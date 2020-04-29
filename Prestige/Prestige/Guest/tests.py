from django.test import TestCase
from .models import Product,Inventory

# Create your tests here.

class InventoryTestCase(TestCase):
    def setUp(self):
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
        Inventory.objects.create(
            size="XS",
            color="Blue",
            quantity="20",
            product = prod
        )
        
    def test_give_size(self):
        obj1 = Inventory.objects.get(size="XS")
        self.assertEqual(obj1.give_size(),"XS")







