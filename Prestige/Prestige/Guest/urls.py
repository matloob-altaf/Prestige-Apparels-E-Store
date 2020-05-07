from django.contrib import admin
from django.urls import path
from . import views

app_name = 'Guest'
urlpatterns = [
    path('', views.index, name="Index"),
    # path('product/addReview', views.addReview, name = "addReview"),
    path('product/<str:slug1>', views.singleProduct, name="product"),
    path('product/', views.singleProduct, name="product"),
    path('catalog/<str:category1>', views.catalog, name="catalog"),
    path('catalog/', views.catalog, name="catalog"),
    path('addReview/<int:id1><user_id1>', views.addReview, name='addReview'),
    path('email/', views.addEmail, name='email'),
    path('visualize', views.qvisualize, name="visualize"),  # page for product visualization

    # for search apperance

    path('cart/', views.view_cart, name="cart"),
    path('update_cart/<str:slug>', views.update_cart, name="update_cart"),
    path('technology/', views.technology, name="technology"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('search', views.search, name="search")

]
