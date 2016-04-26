"""Questionnaires URL Configuration


"""
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^questionnaires/', include('Questionnaires.urls')),               
    url(r'^admin/', admin.site.urls),
]
