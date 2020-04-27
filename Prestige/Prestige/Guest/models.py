from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.



class CategoryChoices(models.Model):
    choice = models.CharField(verbose_name="Add New Category Type", max_length=50)

choices = ['men','women','stain-repellent','anti-odor','upper','bottom','spring-collection', 'summer-collection','winter-collection','autumn-collection']

class Product(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    sale = models.BooleanField(default=1)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null = True, help_text="Leave Blank If there's no discount")
    slug = models.SlugField()
    is_published = models.BooleanField(default=0)
    featured = models.BooleanField(default=1)
    main_img = models.ImageField(upload_to='product/main_images', verbose_name="Product Main Image")  
    sec_img = models.ImageField(upload_to='product/sec_images', blank = True,null = True)
    third_img = models.ImageField(upload_to='product/sec_images', blank = True,null = True)
    fourth_img = models.ImageField(upload_to='product/sec_images', blank = True,null = True)
    tags = models.CharField(max_length=100,help_text="Write all the tags Separated by ',' comma")
    #size = models.ManyToManyField("Variant",editable=True)

    #category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default = 'none')
    category = models.CharField(max_length=300,verbose_name="Add Categories",help_text= "Separate with comma Select from following: " + ", ".join([choice for choice in choices]), blank=True ) #remove blank = True when migrating to final db
    variants : str # dictionary {'color':['red','blue','green'], 'size':['s','m','l']}#size menu #color shown #quantity of each separately

    def category_list(self):
        lst = ",".split(self.category)
        return " ".join(lst)

    
class Inventory(models.Model):
    SIZE_CHOICES = [
        ('XS','XS'),('S','S'), ('M','M'), ('L','L'),('XL','XL'),('XXL','XXL')
    ]
    size = models.CharField(choices= SIZE_CHOICES, max_length=3)
    color = models.CharField(max_length=10)
    quantity = models.SmallIntegerField()
    product = models.ForeignKey("Product", on_delete=models.CASCADE)   
    
    def __str__(self):
        return "PRODUCT: "+ self.product.name + " " +"          SIZE: " +self.size +" " +  self.color +" " + str(self.quantity)

class Newsletter(models.Model):
    email = models.EmailField(max_length=254)

    def __str__(self):
        return str(self.email) 


class Reviews(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Guest.Product",  on_delete=models.CASCADE)
    comments = models.TextField()
    is_visible = models.BooleanField(default=1)
    rating = models.IntegerField()

    #making list against the number of stars in ratings
    def list_rating(self):
        a = []
        for i in range(self.rating):
            a.append('*')
        return a


    def __str__(self):
        return self.user.first_name + "'s Review on " + self.product.name
        #<i class="zmdi zmdi-star-half"></i>

    #will learn what is this
    #def get_absolute_url(self):
    #    return reverse("_detail", kwargs={"pk": self.pk})

"""
class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email : models.EmailField( max_length=254)
    profile_pic = models.ImageField(upload_to='user_profiles')

    # These all will be revised
    address = models.CharField(max_length=300)
    state = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    country = CountryField()
    gender = models.CharField(max_length=100)
    username = models.CharField(max_length=100)  # Need to set
    password = models.CharField(max_length=100)  # Will be changed once study forms forms.PasswordInput
    
        
    def __str__(self):
        return self.first_name + " " + self.last_name

    #def get_absolute_url(self):
    #    return re", kwargs={"pk": self.pk})
"""

class Order(models.Model):
    status_codes = [
        ('p','pending'),('d','delivered'), ('e','enroute')]
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Guest.Product",  on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.PositiveIntegerField(default=0)
    date_time = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=status_codes, max_length=9,default=status_codes[0])
    def __str__(self):
        return str(self.pk) + str(self.user) + self.status
