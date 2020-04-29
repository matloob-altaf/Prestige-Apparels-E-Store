from django.shortcuts import render
from django.http import HttpResponse
from Guest.models import Product
from django.contrib.auth.models import User, auth
from Guest.models import Reviews,Inventory 
from django.db.models import Count
from plotly.offline import plot
from plotly.graph_objs import Bar
from plotly.graph_objects import Layout
from plotly.graph_objects import Figure
from Guest.utilities import creatPlotly





# Create your views here.


def index(request):
    #Check the request if data is to be shown dynamic
    product = Product.objects.filter(featured = True)
    return render(request,'index.html',{'products':product })


#return the product on the template of single product with slug 
def singleProduct(request, slug1):
    product = Product.objects.get(slug = slug1)
    return render(request,'product.html',{'product':product})

"""
def singleProduct(request):
    return render(request,'product.html')
"""

#return the all the products on the shop page template with given category 
def catalog(request, category1=" "):
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

def Cart(request):
    return render(request,'shoping-cart.html')



# Will make a class once all views functions are clear to me
# Customer class here that will be able to handle all the shopping stuff done by customer


def addReview(request):
    if request.method == 'POST':
        comment = request.POST['review']
        rating = request.POST['rating']
        name = request.POST['name']
        email = request.POST['email']
        if (user.is_autheticated):
            user = user
        product = Product.Object.get(slug = request.GET['product'].slug)


        
        
        review = Reviews(user=user, product = product, comments=comment, rating=rating)
        review.save();
        print('Review Added')
        #return redirect('login')
        
        
        #return redirect('register')

        #return redirect('/')
    
        #return render(request, 'register.html')
##########################################################################3

def qvisualize(request):
    plot_div = creatPlotly("size",xtitle="Size",ytitle="Quantity",plot_title="Sizes and their quantity in the inventory")
    plot_div1 = creatPlotly("color",xtitle="Color",ytitle="Quantity",plot_title="Color and their quantity in the inventory")
    context = {'plot_div':plot_div,
                'plot_div1':plot_div1}

    return render(request, "model.html", context=context)

    
    

    
