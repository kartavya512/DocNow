from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    path('loginuser', views.loginuser, name='loginuser'),

    path('registeruser', views.registeruser, name='registeruser'),
    path('user', views.user, name='user'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('departments', views.departments, name='departments'),
    path('doctor', views.doctor, name='doctor'),
    path('about', views.about, name='about'),
    path('appointment', views.appointment, name='appointment'),
    path('logoutuser', views.logoutuser, name='logoutuser'),
    path('videocall', views.videocall, name='videocall'),
    path('videocallUser', views.videocallUser, name='videocallUser'),
    path('success', views.success, name='success')

]
