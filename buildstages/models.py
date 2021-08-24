from django.db import models
from mainbuild.models import MyBuildDescription, MyBuild
from model_utils.managers import InheritanceManager
from django import forms




class BuildStage(models.Model):
    complete = models.BooleanField('Etap zakończony', default=False)
    created = models.DateTimeField(auto_now_add=True)
    stage_name = models.CharField('Nazwa etapu',max_length=150)
    budget = models.FloatField('Zakładany budżet',blank=True, null=True)
    build_id = models.ForeignKey(MyBuild, on_delete=models.CASCADE, blank=True, null=True)
    stage_startdate = models.DateField('Data rozpoczecia etapu', null=True, blank=True)
    stage_enddate = models.DateField('Data zakończenia etapu', null=True, blank=True)
    stage_cost = models.FloatField(blank=True, null=True)
    stage_budget_calculation = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.stage_name

class BuildStageElement(models.Model):
    element_name = models.CharField(max_length=200)
    price = models.PositiveIntegerField(default=0, blank=True, null=True)
    buildstage = models.ForeignKey(BuildStage, related_name='elements', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.element_name
