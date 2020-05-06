from django.contrib import admin
from Guest.models import Product, Customer, Reviews , Orders, Inventory, Newsletter


# Register your models here.

admin.site.register(Product)
admin.site.register(Reviews)
admin.site.register(Orders)
admin.site.register(Inventory)
admin.site.register(Newsletter)
admin.site.register(Customer)
