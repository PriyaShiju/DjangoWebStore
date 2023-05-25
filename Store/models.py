from django.db import models
#from django.urls import reverse
from decimal import Decimal
from django.utils.text import slugify
#from datetime import date


class ProductInStockQuerySet(models.QuerySet):
    def in_stock(self):
        return self.filter(stock_count_gt=0)



# Create your models here.    
class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(max_length=500)
    benefits = models.TextField(blank=True,null=True) ## null = true is for DB and blank=true for html form
    price = models.DecimalField(default=85.00,decimal_places=2, max_digits=4)
    date = models.DateField(auto_now=True)
    stock = models.IntegerField(default=50, help_text="How many items are currentl;y in stock")
    sku = models.CharField(verbose_name="Stock keeping Unit", max_length=20, unique=True) 
    slug = models.SlugField(default="slugfield")
    objects =models.Manager()
    in_stock = ProductInStockQuerySet.as_manager()
    
    def save(self,*args,**kwargs): # overwrting save after checking if slug is empty then assign name to the slug field
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args,**kwargs)
    
    class Meta:
        #proxy = True
        #abstract = True        
        ordering = ['price']       
        constraints=[models.CheckConstraint(check=models.Q(price__gte=0), name="price not negative")]
        
    def get_absolute_url(self):
        return "" #reverse("ProductDetail",kwargs={'pk':self.id})
    
    @property
    def vat(self):
        return Decimal(.2)*self.price    
    
    def __str__(self):
        return f"{self.name} is only ${self.price}"
    
    
class ProductImage(models.Model):
    image = models.ImageField()
    product = models.ForeignKey("Product",on_delete=models.CASCADE)    
    
    def __str__(self):
        return f"{self.image}"
    
"""sumary_line"""

class ProductCategory(models.Model):
    categoryName = models.CharField(max_length=50)
    product = models.ManyToManyField("Product", related_name="categories") # related_name="+"
        
    def __str__(self):
        return f"{self.categoryName}"
    
    class Meta:
        ordering =["categoryName"]
        verbose_name ="Category"
        verbose_name_plural ="Categories"
        
#subclass
class DigitalProduct(Product):
    file = models.FileField()
    
class PhysicalProduct(Product):
    stock_count = models.IntegerField(help_text="How many items are currently in the stock")