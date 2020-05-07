
from django.contrib import admin
from django.urls import path
# from mlmodel.veiws import mlresults
from .views import modelResults

# app_name = 'mlmodel' #Name of the app

#Urls associated with this app
urlpatterns = [
    path('mlresults',modelResults, name='model')
]