from django.db import models

# Create your models here.
"""
class Product(models.Model):
    name : str
    main_img : str #img  
    sec_imgs : str #image field for multiple images
    description : str 
    category : str #list #can be in multiple categories
    reviews : str #list #foriegn key (may be)
    variants : str # dictionary {'color':['red','blue','green'], 'size':['s','m','l']}#size menu #color shown #quantity of each separately
    tags : list
    sale : bool # On Sale/Not
    discount_price : float
    slug : str #used for each product permalink --> Product/{{slug}}
    is_published : bool
    Review : models.ForeignKey("Guest.Reviews", verbose_name=_(""), on_delete=models.CASCADE)


    def __str__(self):
        return self.name


   

class Reviews(models.Model):
    
    user = models.ForeignKey("accounts.User", verbose_name=_(""), on_delete=models.CASCADE)
    product = models.ForeignKey("app.Model", verbose_name=_(""), on_delete=models.CASCADE)
    comments : str
    is_visible : bool
    rating : float

    def __str__(self):
        return self.user.name + "'s Review on " + self.product

    #will learn what is this
    #def get_absolute_url(self):
    #    return reverse("_detail", kwargs={"pk": self.pk})

class User(models.Model):
    first_name : str
    last_name : str
    phone_number : str
    address: str
    state : str
    city: str
    country : str
    username : str
    password : password
    email : models.EmailField(_(""), max_length=254)
    gender : str #-> select from list

    
        
    def __str__(self):
        return self.first_name + " " + self.last_name

    #def get_absolute_url(self):
    #    return re", kwargs={"pk": self.pk})
"""


class Destination(models.Model):

    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    desc = models.TextField()
    price = models.IntegerField()
    offer = models.BooleanField(default=0)
