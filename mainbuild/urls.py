from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'mainbuild'

urlpatterns = [
    path('', views.base, name='home'),
    path('userpanel/', views.MyBuildView.userpanel, name='userpanel'),
    path('addbuild/', views.MyBuildView.addbuild, name='addbuild'),
    path('listbuild/', views.MyBuildListView.as_view(), name='building_list'),
    path('editdescription/<int:id>', views.MyBuildListView.edit_description, name='edit_description'),
    path('delete_build/<int:id>', views.MyBuildView.delete_build, name='delete_build'),
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)