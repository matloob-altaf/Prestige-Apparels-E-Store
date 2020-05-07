from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from Guest.models import Product
from django.contrib.auth.models import User, auth
from Guest.models import Reviews, Newsletter, Inventory
from django.urls import reverse
from django.contrib import messages





def index(request):
    product = Product.objects.filter(featured = True)
    return render(request,'index.html',{'products':product })

# return the product on the template of single product with slug 
def singleProduct(request, slug1):
    product1 = Product.objects.get(slug = slug1)
    reviews = Reviews.objects.filter(product = product1)
    inventorys = Inventory.objects.filter(product = product1).exclude(quantity = 0)
    


    number_reviews = len(reviews)
    return render(request,'product.html',{'product':product1,'reviews':reviews,'len':number_reviews, 'inventory':inventorys})

# return the all the products on the shop page template with given category 
def catalog(request, category1=" "):
    print("catalog called")
    if (category1 != " "):
        product_to_show = Product.objects.filter(category__contains = category1 ) #assuming now that all the categories are added in a single string separated by comma or space
        p1 = Product.objects.filter(name__contains = category1 )
        p2 = Product.objects.filter(description__contains = category1 )
        product_to_show = product_to_show.union(p1.union(p2))
        return render(request,'catalog.html',{'Products':product_to_show})
    else:
        product_to_show = Product.objects.all()
        return render(request,'catalog.html',{'Products':product_to_show})

def technology(request):
    return render(request,'technology.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def cart(request):
    return render(request,'shoping-cart.html')


def search(request):
    text = request.GET['search']
    text = text.lower()
    text = text.split()
    pts = Product.objects.none()

    for x in text:            
        pts = Product.objects.filter(category__contains = x).union(pts) #assuming now that all the categories are added in a single string separated by comma or space
        pts = Product.objects.filter(name__contains = x ).union(pts)
        pts = Product.objects.filter(description__contains = x ).union(pts)
    if not pts:
        messages.info(request,"No product Found") 
        print(messages)
    return render(request,'catalog.html',{'Products':pts})


def addReview(request, id1, user_id1):
    if request.method == 'POST':
        comment = str(request.POST['review'])
        rating = request.POST['rating']
        user1 = User.objects.get(id = user_id1)
        product1 = Product.objects.get(pk = id1)
        
        review = Reviews(user=user1, product = product1, is_visible = True, comments=comment, rating=rating)
        review.save();

        print('Review Added')

        return redirect('Guest:product',product1.slug)


def addEmail(request):
    if request.method == 'POST':
        email1 = str(request.POST['email'])
        
        email2 = Newsletter(email = email1)
        email2.save();

        print('Email Added')

        #return redirect('Guest:product',product1.slug)
        #return redirect(request.path)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '#'))