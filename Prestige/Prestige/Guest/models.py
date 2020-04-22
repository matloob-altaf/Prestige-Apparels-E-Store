from django.db import models
from django_countries.fields import CountryField
from django.contrib.auth.models import User

# Create your models here.




class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    sale = models.BooleanField(default=0)
    price = models.FloatField()
    discount_price = models.FloatField()
    slug = models.SlugField
    is_published = models.BooleanField(default=0)
    main_img = models.ImageField(upload_to='product/main_images')  
    sec_imgs = models.ImageField(upload_to='product/sec_images')

    #These all will be revised
    category : str #list #can be in multiple categories
    variants : str # dictionary {'color':['red','blue','green'], 'size':['s','m','l']}#size menu #color shown #quantity of each separately
    tags = models.CharField(max_length=100)
    
    

    def __str__(self):
        return self.name



class Reviews(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey("Guest.Product",  on_delete=models.CASCADE)
    comments = models.TextField()
    is_visible = models.BooleanField(default=1)
    rating = models.FloatField()


    def __str__(self):
        return self.user.name + "'s Review on " + self.product

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

    def __str__(self):
        name : str
        return self.name
