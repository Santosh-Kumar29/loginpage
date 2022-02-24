from django.contrib import admin
from django.urls import path, include
from . import views

from login_form import views

urlpatterns = [
    path('login_adddata/', views.login_adddata, name='login_adddata'),
    path('login_getdata/', views.login_getdata, name='login_getdata'),
    path('login_isactivaedata/', views.login_isactivaedata, name='login_isactivaedata'),
    path('login_isactiveput/', views.login_isactiveput, name='login_isactiveput'),
]