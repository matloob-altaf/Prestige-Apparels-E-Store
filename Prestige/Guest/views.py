from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from Guest.models import Product, Cart, CartItem, Orders
from django.contrib.auth.models import User, auth
from Guest.models import Reviews, Newsletter, Inventory
from django.urls import reverse
from django.utils.crypto import get_random_string
from django.contrib import messages
from plotly.offline import plot
from plotly.graph_objs import Bar
from plotly.graph_objects import Layout
from plotly.graph_objects import Figure
from Guest.utilities import creatPlotly


def index(request):
    product = Product.objects.filter(featured=True)
    return render(request, 'index.html', {'products': product})


# return the product on the template of single product with slug
def singleProduct(request, slug1):
    product1 = Product.objects.get(slug=slug1)
    reviews = Reviews.objects.filter(product=product1)
    inventorys = Inventory.objects.filter(product=product1).exclude(quantity=0).exclude(active=False)
    colors = list(set(inventorys.values_list('color', flat=True)))
    sizes = list(set(inventorys.values_list('size', flat=True)))
    quantity = inventorys.values_list('quantity', flat=True)
    if (not quantity):
        quantity = 0
    else:
        quantity = quantity[0]

    number_reviews = len(reviews)
    return render(request, 'product.html',
                  {'product': product1, 'reviews': reviews, 'len': number_reviews, 'colors': colors, 'sizes': sizes, 'qauntity': quantity})


# return the all the products on the shop page template with given category
def catalog(request, category1=" "):
    print("catalog called")
    if (category1 != " "):
        product_to_show = Product.objects.filter(
            category__contains=category1)  # assuming now that all the categories are added in a single string separated by comma or space
        p1 = Product.objects.filter(name__contains=category1)
        p2 = Product.objects.filter(description__contains=category1)
        product_to_show = product_to_show.union(p1.union(p2))
        return render(request, 'catalog.html', {'Products': product_to_show})
    else:
        product_to_show = Product.objects.all()
        return render(request, 'catalog.html', {'Products': product_to_show})


def technology(request):
    return render(request, 'technology.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def view_cart(request):
    try:
        the_id = request.session['cart_id']
    except:
        the_id = None
        print("here")
    if the_id:
        cart = Cart.objects.get(id=the_id)
        new_total = 0.00
        for item in cart.cartitem_set.all():
            per_item_total = item.product.price * item.quantity
            item.sub_total = per_item_total
            item.save()
            new_total += per_item_total
        request.session['item_total'] = cart.cartitem_set.all().count()
        cart.total = new_total
        # print(cart.cartitem_set.all().count())

        cart.save()
        if cart.cartitem_set.all().count() != 0:
            context = {"cart": cart}
        else:
            context = {'empty': True}
            messages.info(request, "Empty cart please keep shopping")
    else:
        context = {'empty': True}
        messages.info(request, "Empty cart please keep shopping")
    template = "shoping-cart.html"
    # print(cart.items)
    return render(request, template, context)

def remove_from_cart(request, id):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        messages.error(request, 'Unexpected error occured!')
        return redirect('Guest:cart')
    cart_item = CartItem.objects.get(id=id)
    # cart_item.cart = None
    # cart_item.save()
    variant = Inventory.objects.get(id=cart_item.variation.id)
    variant.quantity += cart_item.quantity
    variant.save()
    cart.total -= cart_item.sub_total
    cart.save()
    cart_item.delete()
    messages.success(request, 'Item Successfully removed from cart')
    return redirect('Guest:cart')

def update_cart(request, slug):

    variation_types = []
    try:
        the_id = request.session['cart_id']
        print("no heer", the_id)
    except:
        new_cart = Cart()
        new_cart.save()
        request.session['cart_id'] = new_cart.id
        the_id = new_cart.id
        print("here", the_id)
    #
    cart = Cart.objects.get(id=the_id)

    try:
        product = Product.objects.get(slug=slug)
        print(product)
    except Product.DoesNotExist:
        pass
    except:
        pass
    if request.method == "POST":
        # print(request.POST)
        qty = request.POST['qty']
        color = request.POST['color']
        size = request.POST['size']
        try:
            v = Inventory.objects.filter(product=product).filter(size=size).filter(color=color)
            variation_types.append(v.values_list('color', flat=True)[0])
            variation_types.append(v.values_list('size', flat=True)[0])
        except:
            pass
    if request.method=="GET":
        qty = request.GET.get('qty')

    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product, variation=v[0])


    if int(qty):
        cart_item.quantity = int(qty)
        v = v[0]
        v.quantity -= int(qty)
        v.save()
        cart_item.save()


    return redirect('Guest:cart')

def checkout(request):
    try:
        the_id = request.session['cart_id']
        cart = Cart.objects.get(id=the_id)
    except:
        the_id = None
        return redirect("Guest:cart")
    new_order, created = Orders.objects.get_or_create(cart=cart)
    if created:
        new_order.order_id = "PRESTIGE"+get_random_string(5)
        new_order.save()
    if new_order.status == "IN PROCESS":
        del request.session['cart_id']
        del request.session['item_total']
        return redirect("Guest:cart")
    context = {}
    template = "checkout.html"
    return redirect("Guest:cart")

def orders(request):
    context = {}
    template = "user.html"
    return render(request, template, context)
def search(request):
    text = request.GET['search']
    text = text.lower()
    text = text.split()
    pts = Product.objects.none()

    for x in text:
        pts = Product.objects.filter(category__contains=x).union(
            pts)  # assuming now that all the categories are added in a single string separated by comma or space
        pts = Product.objects.filter(name__contains=x).union(pts)
        pts = Product.objects.filter(description__contains=x).union(pts)
    if not pts:
        messages.info(request, "No product Found")
        print(messages)
    return render(request, 'catalog.html', {'Products': pts})


def addReview(request, id1, user_id1):
    if request.method == 'POST':
        comment = str(request.POST['review'])
        rating = request.POST['rating']
        user1 = User.objects.get(id=user_id1)
        product1 = Product.objects.get(pk=id1)

        review = Reviews(user=user1, product=product1, is_visible=True, comments=comment, rating=rating)
        review.save();

        print('Review Added')

        return redirect('Guest:product', product1.slug)


def addEmail(request):
    if request.method == 'POST':
        email1 = str(request.POST['email'])

        email2 = Newsletter(email=email1)
        email2.save();

        print('Email Added')

        # return redirect('Guest:product',product1.slug)
        # return redirect(request.path)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '#'))


def qvisualize(request):
    '''function to produce plots of various products'''
    plot_div = creatPlotly("size", xtitle="Size", ytitle="Quantity",
                           plot_title="Sizes and their quantity in the inventory")
    plot_div1 = creatPlotly("color", xtitle="Color", ytitle="Quantity",
                            plot_title="Color and their quantity in the inventory")
    context = {'plot_div': plot_div,
               'plot_div1': plot_div1}
    return render(request, "model.html", context=context)




