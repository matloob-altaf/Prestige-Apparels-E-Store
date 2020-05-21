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

###############################################################################################################333

#from django.test import TestCase
from .models import Product,Inventory,Reviews
#from django.urls import reverse,resolve

# Create your tests here.

class InventoryTestCase(TestCase):
    '''class to test Inventory model'''
    def setUp(self):
        '''baseline function to create objects for testing'''
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
        prod2 = Product.objects.create(
            name = "MyProduct1",
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
        Inventory.objects.create(
            size="XS",
            color="Blue",
            quantity="20",
            product = prod
        )
    def test_give_size(self):
        '''function to test give_size function of model'''
        obj1 = Inventory.objects.get(size="XS")
        self.assertEqual(obj1.give_size(),"XS")
        self.assertNotEqual(obj1.give_size(),"S")
        self.assertNotEqual(obj1.give_size(),"M")
        self.assertNotEqual(obj1.give_size(),"L")
        self.assertNotEqual(obj1.give_size(),"XL")
        self.assertNotEqual(obj1.give_size(),"XXL")
    def test_give_color(self):
        '''function to test give_color function'''
        obj1 = Inventory.objects.get(color="Blue")
        self.assertAlmostEqual(obj1.give_color(),"Blue")
        colorList = ["Brown","Gray","Pink","Red","Green","Purple"]
        for color in colorList:
            self.assertNotEqual(obj1.give_color(),color)
    def test_give_quantity(self):
        '''function to test give_quantity function'''
        obj1 = Inventory.objects.get(quantity=20)
        self.assertEqual(obj1.give_quantity(),20)
        for i in range(0,100):
            if i==20:
                continue
            else:
                self.assertNotEqual(obj1.give_quantity(),i)
                
    def test_give_product(self):
        obj1 = Product.objects.get(name="MyProduct")
        obj2= Inventory.objects.get(product= obj1)
        self.assertEqual(obj2.give_product(), obj1)
        obj3= Product.objects.get(name="MyProduct1")
        self.assertNotEqual(obj2.give_product(), obj3)
        
        
class ProductTestCase(TestCase):
    '''class to test product model'''
    def setUp(self):
        '''function to create objects for tests'''
        Product.objects.create(
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
    def test_name(self):
        '''function to test give name function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_name(),"MyProduct")
        self.assertNotEqual(obj1.give_name(),"NotMyProductName")
    def test_description(self):
        '''function to test give_description function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_description(),"My beautiful product")
        self.assertNotEqual(obj1.give_description(),"Not my project description")
    def test_sale(self):
        '''function to test give_sale function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_sale(),True)
        self.assertNotEqual(obj1.give_sale(),False)
    def test_price(self):
        '''function to test give_price function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_price(),2500)
        self.assertNotEqual(obj1.give_price(),300)
    def test_discount_price(self):
        '''function to test give_discount function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_discount_price(),1000)
        self.assertNotEqual(obj1.give_discount_price(),1100)
    def test_slug(self):
        '''function to test give_slug function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_slug(),"MySlug")
        self.assertNotEqual(obj1.give_slug(),"Not My Slug")
    def test_is_published(self):
        '''function to test is_published function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_published(),True)
        self.assertNotEqual(obj1.give_published(),False)
    def test_featured(self):
        '''function to test is_featured function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_featured(),True)
        self.assertNotEqual(obj1.give_featured(),False)
    def test_mainimg(self):
        '''function to test give_mainimg function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_mainimg(),"my image")
        self.assertNotEqual(obj1.give_mainimg(),"not my main image")
    def test_secimg(self):
        '''function to test give_secimg function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_secimg(),"sec img")
        self.assertNotEqual(obj1.give_secimg(),"Not my sec image")
    def test_thirdimg(self):
        '''function to test give_thirdimg function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_thirdimg(),"third img")
        self.assertNotEqual(obj1.give_thirdimg,"Not my third image")
    def test_fourthimg(self):
        '''function to test give_fourthimg function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_fourthimg(),"fourth img")
        self.assertNotEqual(obj1.give_fourthimg(),"Not m fourth image")
    def test_tags(self):
        '''function to test give_tags function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_tags(),"lol tag")
        self.assertNotEqual(obj1.give_tags(),"not my favourite tag")
    def test_category(self):
        '''function to test give_category function'''
        obj1 = Product.objects.get(name="MyProduct")
        self.assertEqual(obj1.give_category(),"my category")
        self.assertNotEqual(obj1.give_category(),"Men categoory")
class TestUrl(TestCase):
    '''class to test url resolution by testing app name and views names'''
    def test_resolution_for_apps(self):
        '''function to test for resolution of apps'''
        listPaths = ['/','/product/','/catalog/','/visualize','/cart/','/technology/','/about/','/contact/',
        '/product/<str:slug1','/catalog/<str:category1>']
        for path in listPaths:
            resolver = resolve(path)
            self.assertEqual(resolver.app_name,'Guest')
    def test_resolution_for_viewsNames(self):
        '''function to test for resolution of view/functions'''
        listPaths = ['/','/product/','/catalog/','/visualize','/cart/','/technology/','/about/','/contact/',
        '/product/<str:slug1','/catalog/<str:category1>']
        listPaths1 = ['Index','product','catalog','visualize','cart','technology','about','contact','product','catalog']
        for viewname,url in zip(listPaths1,listPaths):
            resolver = resolve(url)
            self.assertEqual(resolver.view_name,resolver.app_name+":"+viewname)

        
        



        








