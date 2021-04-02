from django.urls import path
from django.contrib.auth import views as auth_views

from models.bases.views import Home

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'),
        name='login'),
    #funciona para el deslogeo
    path('logout/', auth_views.LogoutView.as_view(template_name='bases/login.html'), name='logout'),

]