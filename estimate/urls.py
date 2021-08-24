from django.urls import path
from . import views

app_name = 'estimate'

urlpatterns = [
    path('myestimate/', views.Estimate.as_view(), name="estimate"),

    ]
