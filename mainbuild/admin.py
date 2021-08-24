from django.contrib import admin
from .models import MyBuildDescription, MyBuild
# Register your models here.

admin.site.register(MyBuildDescription)
admin.site.register(MyBuild)

