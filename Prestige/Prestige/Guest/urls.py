from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name = "Index"),
    path('Product/<str : slug1>', views.singleProduct, name = "single_product"),
    path('Catalog/<str : category1>', views.catalog, name = "catalog"),
    
    # for search apperance
    # path('Catalog/<str : slug', views.singleProduct, name = "single_product"),
    
    path('Cart/', views.shoppingCart, name = "shopping"),
    path('Technology/', views.technology, name = "technology"),
    path('about/', views.about, name = "about")

]
