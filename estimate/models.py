from django.db import models
from django.contrib.auth.models import User
from mainbuild.models import MyBuild
from buildstages.models import BuildStage, BuildStageElement

# Create your models here.
class UserEstimate(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

