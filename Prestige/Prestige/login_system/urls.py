from django.contrib import admin
from django.urls import path
from . import views


app_name = 'login_system'
urlpatterns = [
    path('login/', views.login, name = "login"),
    path('login/<str:next>', views.login, name = "login"),
    path('signup/', views.signup, name = "signup"),
    path('customer/', views.customerAccount, name = "customer"),
    path('logout/', views.logout, name = "logout"),


]
