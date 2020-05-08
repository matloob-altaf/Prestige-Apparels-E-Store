from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.


class CategoryChoices(models.Model):
    choice = models.CharField(verbose_name="Add New Category Type", max_length=50)


choices = ['men', 'women', 'stain-repellent', 'anti-odor', 'upper', 'bottom', 'spring-collection', 'summer-collection',
           'winter-collection', 'autumn-collection']


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sale = models.BooleanField(default=1)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True, help_text="Leave Blank If there's no discount")
    slug = models.SlugField()
    is_published = models.BooleanField(default=0)
    featured = models.BooleanField(default=1)
    main_img = models.ImageField(upload_to='product/main_images', verbose_name="Product Main Image")
    sec_img = models.ImageField(upload_to='product/sec_images', blank=True, null=True)
    third_img = models.ImageField(upload_to='product/sec_images', blank=True, null=True)
    fourth_img = models.ImageField(upload_to='product/sec_images', blank=True, null=True)
    tags = models.CharField(max_length=100, help_text="Write all the tags Separated by ',' comma")
    # size = models.ManyToManyField("Variant",editable=True)

    # category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default = 'none')
    category = models.CharField(max_length=300, verbose_name="Add Categories",
                                help_text="Separate with comma Select from following: " + ", ".join(
                                    [choice for choice in choices]),
                                blank=True)  # remove blank = True when migrating to final db

    def category_list(self):
        lst = ",".split(self.category)
        return " ".join(lst)

    def __str__(self):
        return self.name


class Inventory(models.Model):
    SIZE_CHOICES = [
        ('XS', 'XS'), ('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), ('XXL', 'XXL')
    ]
    size = models.CharField(choices=SIZE_CHOICES, max_length=3)
    color = models.CharField(max_length=10)
    quantity = models.SmallIntegerField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)

    def __str__(self):
        return "PRODUCT: " + self.product.name + " " + "          SIZE: " + self.size + " " + self.color + " " + str(
            self.quantity)


class Newsletter(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.email)


class Reviews(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Guest.Product", on_delete=models.CASCADE)
    comments = models.TextField()
    is_visible = models.BooleanField(default=1)
    rating = models.IntegerField()

    # making list against the number of stars in ratings
    def list_rating(self):
        a = []
        for i in range(self.rating):
            a.append('*')
        return a

    def __str__(self):
        return self.user.first_name + "'s Review on " + self.product.name
        # <i class="zmdi zmdi-star-half"></i>

    # will learn what is this
    # def get_absolute_url(self):
    #    return reverse("_detail", kwargs={"pk": self.pk})


class Customer(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    phone_number = PhoneNumberField(null=False, blank=False)
    address = models.TextField(blank=True, null=True)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=1, default='O')

    def _str_(self):
        return str(self.user.email)


class Orders(models.Model):
    STATUS_CHOICES = [
        ('IN PROCESS', 'In Process'),
        ('SHIPPED', 'Shipped'),
        ('RECEIVED', 'Received')
    ]
    customer = models.ForeignKey("Guest.Customer", on_delete=models.CASCADE)
    product = models.ManyToManyField("Guest.Product")
    status = models.CharField(choices=STATUS_CHOICES, max_length=15, default='IN PROCESS')
    order_date = models.DateField(auto_now=False, auto_now_add=True)
    order_time = models.TimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "ORDER ID: " + str(self.pk) + " -------  CUSTOMER: " + str(
            self.customer.user.username) + " --------- " + str(self.product.all()) + " ---------  ORDER DATE: " + str(
            self.order_date) + " ---------  DELIVERY STATUS: " + str(self.status)


class CartItem(models.Model):
    cart = models.ForeignKey('Cart', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    sub_total = models.DecimalField(default=0.00, max_digits=100, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.product.title


class Cart(models.Model):
    # items = models.ManyToManyField(CartItem)
    # product = models.ManyToManyField(Product)
    total = models.DecimalField(max_length=100, decimal_places=2, max_digits=100, default=0.0)
    timestamp = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=1)

    def __str__(self):
        return str(self.pk)