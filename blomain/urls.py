from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from mainbuild import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mainbuild.urls', namespace='mainbuild')),
    path('', include('buildstages.urls', namespace='buildstages')),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
]
