"""
Definition of urls for MegaSena.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views


urlpatterns = [
    path('', views.home, name='home'),
    path('<str:num1>/<str:num2>/<str:num3>/<str:num4>/<str:num5>/<str:num6>', views.result, name='result')
]
