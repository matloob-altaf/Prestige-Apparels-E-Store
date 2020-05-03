from django.contrib import admin
from django.urls import path
from . import views


app_name = 'mlmodel' #Name of the app


#Urls associated with this app
urlpatterns = [
    path('mlresults',views.modelResults, name='model')
]