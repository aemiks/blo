from django.shortcuts import render, reverse, redirect, HttpResponseRedirect, get_object_or_404
from django.views.generic import ListView, View, TemplateView, DetailView
from .models import BuildStage, BuildStageElement
from .forms import BuildStageElementForm, BuildStageForm
from mainbuild.models import MyBuild
from django.contrib import messages


class BuildStagesDetailView(DetailView):
    template_name = 'buildstages/build_stages.html'
    model = BuildStage

    def get(self, request, *args, **kwargs):
        object = MyBuild.objects.filter(id=self.kwargs['id']).get()
        nick = request.user
        build_stages = BuildStage.objects.filter(build_id=object.id)

        ## Stage cost calculation ##
        for stage in build_stages:
            elements_cost = 0
            for element in stage.elements.all():
                elements_cost = elements_cost + element.price
            stage.stage_cost = elements_cost
            stage.save()

        ## stage used budget calculation (to progress bar)##
        for stage in build_stages:
            if stage.stage_cost and stage.budget:
                used_budget = (stage.stage_cost*100)/stage.budget
                used_budget = int(round(used_budget, 0))
                stage.stage_budget_calculation = used_budget
                stage.save()
            else:
                stage.stage_budget_calculation = 0

        ## build cost - calculation ##
        object.build_cost = 0
        for stage in build_stages:
            object.build_cost = object.build_cost + stage.stage_cost
            object.save()

        ## used budget - whole build (circle progress bar) ##
        if object.build_cost and object.budget:
            used_budget = int(round((object.build_cost*100)/object.budget, 0))
            object.budget_calculation = used_budget
            object.save()

        return render(request, self.template_name, {'object':object, 'nick':nick, 'build_stages':build_stages })

    def add_stages(request, **kwargs):
        add_stage_input = request.POST['add_stage']
        object = MyBuild.objects.filter(id=kwargs['id']).get()

        if add_stage_input:
            build_stage = BuildStage.objects.create(build_id=object, stage_name=add_stage_input)
            build_stage.save()
        return HttpResponseRedirect(reverse('buildstages:build_stages', args=[object.id]))

    def add_material(request, **kwargs):
        add_material_input = request.POST['add_material']
        add_material_price_input = request.POST['add_material_price']
        stage = BuildStage.objects.filter(id=kwargs['id']).get()
        object = MyBuild.objects.filter(id=stage.build_id.id).get()


        ## adding element in stage ##
        if add_material_price_input != "":
            element = BuildStageElement.objects.create(element_name=add_material_input, price=add_material_price_input, buildstage=stage)
            element.save()
            messages.success(request, 'Pozytywnie dodano materiał lub usługę!',extra_tags='alert alert-success')
            return HttpResponseRedirect(reverse('buildstages:build_stages', args=[object.id]))
        elif add_material_price_input == "":
            element = BuildStageElement.objects.create(element_name=add_material_input, price=0, buildstage=stage)
            element.save()
            messages.success(request, 'Pozytywnie dodano materiał lub usługę!', extra_tags='alert alert-success')
        return HttpResponseRedirect(reverse('buildstages:build_stages', args=[object.id]))

    def delete_element(request, **kwargs):
        element = BuildStageElement.objects.filter(id=kwargs['id']).get()
        stage = BuildStage.objects.filter(id=element.buildstage.id).get()
        object = MyBuild.objects.filter(id=stage.build_id.id).get()

        if request.POST['delete'] == "":
            element.delete()
            messages.warning(request, 'usunięto element', extra_tags='alert alert-danger')
            return HttpResponseRedirect(reverse('buildstages:build_stages', args=[object.id]))


    def edit_stage(request, **kwargs):
        stage = get_object_or_404(BuildStage, id=kwargs['id'])
        object = MyBuild.objects.filter(id=stage.build_id.id).get()

        form = BuildStageForm(request.POST or None, instance=stage)

        if form.is_valid():
            stage = form.save()
            return HttpResponseRedirect(reverse('buildstages:build_stages', args=[object.id]))

        return render(request, 'buildstages/editstage.html', {'form':form} )

    def delete_stage(request, **kwargs):
        stage = get_object_or_404(BuildStage, id=kwargs['id'])
        object = MyBuild.objects.filter(id=stage.build_id.id).get()

        if request.method == "POST":
            stage.delete()
            return HttpResponseRedirect(reverse('buildstages:build_stages', args=[object.id]))

        return render(request, 'buildstages/confirm_delete_stage.html', {'stage': stage, 'object': object})


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        return context


class BuildStageElementDetailView(DetailView):
    model = BuildStageElement

    def edit_element(request, **kwargs):
        element = get_object_or_404(BuildStageElement, id=kwargs['id'])
        stage = element.buildstage
        object = MyBuild.objects.filter(id=stage.build_id.id).get()

        element_name_edit = request.POST['ele_name_edit']
        element_price_edit = request.POST['ele_price_edit']

        ## editting element in stage - logic  ##
        if element_price_edit:
            element_price_edit = int(element_price_edit)
        else:
            element_price_edit == 0

        if element_name_edit == "" and element_price_edit == '':
            return HttpResponseRedirect(reverse('buildstages:build_stages', args=[object.id]))
        elif element_name_edit != "" and element_price_edit == '':
            element.element_name=element_name_edit
            element.save()
            return HttpResponseRedirect(reverse('buildstages:build_stages', args=[object.id]))
        elif element_name_edit == "" and element_price_edit != '':
            element.price=element_price_edit
            element.save()
            return HttpResponseRedirect(reverse('buildstages:build_stages', args=[object.id]))
        else:
            element.element_name= element_name_edit
            element.price= element_price_edit
            element.save()
            return HttpResponseRedirect(reverse('buildstages:build_stages', args=[object.id]))

