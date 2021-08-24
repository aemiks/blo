from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'buildstages'

urlpatterns = [
    path('build_stages/<int:id>', views.BuildStagesDetailView.as_view(), name='build_stages'),
    path('add_stages/<int:id>/', views.BuildStagesDetailView.add_stages, name='add_stages'),
    path('add_material/<int:id>/', views.BuildStagesDetailView.add_material, name='add_material'),
    path('edit_element/<int:id>/', views.BuildStageElementDetailView.edit_element, name='edit_element'),
    path('edit_stage/<int:id>/', views.BuildStagesDetailView.edit_stage, name='edit_stage'),
    path('delete_element/<int:id>', views.BuildStagesDetailView.delete_element, name='delete_element'),
    path('delete_stage/<int:id>', views.BuildStagesDetailView.delete_stage, name='delete_stage'),
]
