from django.contrib import admin
from django.urls import path
from . import views


app_name = 'mlmodel'

urlpatterns = [
    path('mlresults',views.modelResults, name='model')
]