from django.test import TestCase
from .models import Product,Inventory,Reviews,Cart,CartItem
from django.urls import reverse,resolve
from datetime import datetime


class CartTestCase(TestCase):
    def setUp(self):
        Cart.objects.create(
            total=100,
            timestamp= datetime.now(),
            last_updated= datetime.now(),
            active=1
            
        )
    def test_give_total(self):
        obj1= Cart.objects.get(total=100)
        self.assertEqual(obj1.give_total(), 100)
        for i in range (1000):
            if (i==100):
                continue
            self.assertNotEqual(obj1.give_total(), i)
    """ def test_give_timestamp(self):
        t= datetime.now()
        obj1= Cart.objects.get(timestamp=t)
        self.assertEqual(obj1.give_timestamp(),t) """
        
    def test_give_active(self):
        obj1= Cart.objects.get(active=1)
        self.assertEqual(obj1.give_active(), 1)
        self.assertNotEqual(obj1.give_active(),0)
        
class CartItemTestCase(TestCase):
    def setUp(self):
        mycart= Cart.objects.create(
            total=100,
            timestamp= datetime.now(),
            last_updated= datetime.now(),
            active=1
            
        )
        mycart2= Cart.objects.create(
            total=150,
            timestamp= datetime.now(),
            last_updated= datetime.now(),
            active=1
            
        )
        prod = Product.objects.create(
            name = "MyProduct",
            description = "My beautiful product",
            sale = True ,
            price = 2500,
            discount_price = 1000,
            slug = "MySlug",
            is_published = True,
            featured = True,
            main_img = "my image",
            sec_img = "sec img",
            third_img = "third img",
            fourth_img = "fourth img",
            tags = "lol tag",
            category = "my category"
        )
        invent= Inventory.objects.create(
            size="XS",
            color="Blue",
            quantity="20",
            product = prod
        )
        invent2= Inventory.objects.create(
            size="M",
            color="Blue",
            quantity="20",
            product = prod
        )
        CartItem.objects.create(
            cart= mycart,
            product= prod,
            quantity= 2,
            sub_total= 5000.0, 
            variation= invent,
            timestamp= datetime.now(),
            last_updated= datetime.now()
            
        )
    def test_give_cart(self):
        obj1= Cart.objects.get(total=100)
        obj2 = CartItem.objects.get(cart= obj1)
        obj3= Cart.objects.get(total=150)
        self.assertNotEqual(obj2.give_cart(), obj3)
        #self.assertEqual(obj2.give_cart(), obj1)
        
            
    def test_give_quantity(self):
        obj1= CartItem.objects.get(quantity=2)
        for i in range (50):
            if (i==2):
                self.assertEqual(obj1.give_quantity(), i)
                continue
            self.assertNotEqual(obj1.give_quantity(),i)  
                  
    def test_give_sub_total(self):
        obj1= CartItem.objects.get(sub_total=5000.0)
        self.assertEqual(obj1.give_sub_total(), 5000.0)
        self.assertNotEqual(obj1.give_sub_total(),7000.0)
        
    def test_give_variation(self):
        obj1= Inventory.objects.get(size='XS')
        obj2= CartItem.objects.get(variation=obj1)
        self.assertEqual(obj2.give_variation(), obj1)
        obj3= Inventory.objects.get(size='M')
        self.assertNotEqual(obj2.give_variation(), obj3)
        