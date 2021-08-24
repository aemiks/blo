from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from django.contrib.auth import authenticate, login
from .models import  MyBuildDescription, MyBuild
from .forms import MyBuildDescriptionForm, RegisterForm, MyBuildForm, MyBuildFormEdit
from django.views.generic import ListView, View, TemplateView, DetailView

class UserRegisterView(View):
    """User register"""
    form_class = RegisterForm
    template_name = 'registration/register.html'

    def get(self, request):
        register_form = self.form_class(None)
        return render(request, self.template_name, {'register_form': register_form})

    def post(self, request):
        register_form = self.form_class(request.POST)

        if register_form.is_valid():
            user = register_form.save(commit=False)

            username = register_form.cleaned_data['username']
            password = register_form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('../')

        return render(request, 'index.html', {'register_form': register_form})

def base(request):
    return render(request, 'index.html')

class MyBuildView(View):
    template_name = 'build/mybuild_list.html'

    def userpanel(request):
        return render(request, 'build/mybuild_list.html')

    def addbuild(request):
        form = MyBuildForm(request.POST or None, request.FILES or None)

        if form.is_valid():
            data = form.cleaned_data
            user_form = MyBuild.objects.create(**data, user=request.user)

            return redirect('mainbuild:building_list')

        context = {
            'form': form,
        }
        return render(request, 'build/addbuild.html', context)

    def mybuild(request):
        form = MyBuildDescriptionForm(request.POST or None)

        if form.is_valid():
            form.save()

        context = {
            'form': form,
        }
        return render(request, 'build/userpanel.html', context)

    def delete_build(request, id):
        build = get_object_or_404(MyBuild, pk=id)

        if request.method == "POST":
            build.delete()
            return redirect("mainbuild:building_list")

        return render(request, 'build/confirm_delete.html', {'build':build})


class MyBuildListView(ListView):
    template_name = 'build/mybuild_list.html'
    queryset = MyBuild.objects.all()

    def edit_description(request, id):
        build = get_object_or_404(MyBuild, pk=id)

        try:
            description = build.description
        except MyBuildDescription.DoesNotExist:
            description = None

        form = MyBuildFormEdit(request.POST or None, request.FILES or None, instance=build)
        form_description = MyBuildDescriptionForm(request.POST or None, instance=description)

        if all((form.is_valid(), form_description.is_valid())):
            build = form.save(commit=False)
            description = form_description.save()
            build.description = description
            build.save()
            return redirect("mainbuild:building_list")

        context = {
            'build': build,
            'form': form,
            'form_description': form_description,
        }
        return render(request, 'build/adddescription.html', context)


    def get_context_data(self, **kwargs):
        self.userbuild_list = MyBuild.objects.filter(user=self.request.user)

        context = super().get_context_data(**kwargs)
        context['userbuild_list'] = self.userbuild_list
        return context
