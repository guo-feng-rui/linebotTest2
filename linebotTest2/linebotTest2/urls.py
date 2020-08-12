"""
Definition of urls for linebotTest2.
"""

from datetime import datetime
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^callback',views.callback),
]
