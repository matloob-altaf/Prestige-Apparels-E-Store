from django.contrib import admin
from django.urls import path
from . import views



#Name of the current app
app_name = 'Guest'

#List of url patterns for app=Gues
urlpatterns = [
    path('', views.index, name = "Index"), #default page
    path('product/<str:slug1>', views.singleProduct, name = "product"), #single product page
    path('product/', views.singleProduct, name = "product"), #default single product page
    path('catalog/<str:category1>', views.catalog, name = "catalog"), #catalog with category page
    path('catalog/', views.catalog, name = "catalog"), #default catalog page
    path('addReview',views.addReview, name='addreview'), #add review page
    path('visualize',views.qvisualize,name="visualize"), #page for product visualization
    path('cart/', views.Cart, name = "shopping"), #page for cart
    path('technology/', views.technology, name = "technology"), #page for technology used
    path('about/', views.about, name = "about"), #page for about the store
    path('contact/', views.about, name = "contact"),#page to contact in case of any problem
    
]
