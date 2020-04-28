from django.contrib import admin
from django.urls import path
from . import views



app_name = 'Guest'
urlpatterns = [
    path('', views.index, name = "Index"),
    path('product/<str:slug1>', views.singleProduct, name = "product"),
    path('product/', views.singleProduct, name = "product"),
    path('catalog/<str:category1>', views.catalog, name = "catalog"),
    path('catalog/', views.catalog, name = "catalog"),
    path('addReview',views.addReview, name='addreview'),
    #Need to move visualize to admin after admin app is created
    path('visualize',views.qvisualize,name="visualize"),
    
    # for search apperance
    
    
    path('cart/', views.Cart, name = "shopping"),
    path('technology/', views.technology, name = "technology"),
    path('about/', views.about, name = "about"),
    path('contact/', views.about, name = "contact"),
    

]
