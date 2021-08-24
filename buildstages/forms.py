from .models import BuildStageElement, BuildStage
from django import forms

class DateInput(forms.DateInput):
    input_type = 'date'

class BuildStageForm(forms.ModelForm):
    stage_startdate = forms.DateField(label='Data rozpoczęcia etapu', widget=DateInput)

    class Meta:
        model = BuildStage
        exclude = ['build_id', 'stage_cost', 'stage_budget_calculation','stage_enddate']
        fields = '__all__'



class BuildStageElementForm(forms.ModelForm):
    class Meta:
        model = BuildStageElement
        fields = ['element_name', 'price']
