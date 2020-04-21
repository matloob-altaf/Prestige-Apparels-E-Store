from django.shortcuts import render
from django.http import HttpResponse
from models import Product



# Create your views here.


def index(request):
    #Check the request if data is to be shown dynamic
    return render(request,'index.html')

#return the product on the template of single product with slug 
def singleProduct(request, slug1):
    product_to_show = Product.objects.get(slug = slug1)
    return render(request,'product.html',{'Product':product_to_show})

#return the all the products on the shop page template with given category 
def catalog(request, category1):
    product_to_show = Product.objects.filter(category__contains = category1 ) #assuming now that all the categories are added in a single string separated by comma or space
    p1 = Product.objects.filter(name__contains = category1 )
    p2 = Product.objects.filter(description__contains = category1 )
    product_to_show = product_to_show.union(p1.union(p2))
    return render(request,'catalog.html',{'Products':product_to_show})

def technology(request):
    return render(request,'technology.html')

def about(request):
    return render(request,'about.html')

def Cart(request):
    return render(request,'shoping-cart.html')



# Will make a class once all views functions are clear to me
# Customer class here that will be able to handle all the shopping stuff done by customer


