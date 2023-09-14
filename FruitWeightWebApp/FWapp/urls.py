from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('detection/', views.detection, name="detection"),
    path('login/', views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('register/',views.registerPage, name="register"),

]


