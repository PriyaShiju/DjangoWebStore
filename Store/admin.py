from django.contrib import admin
from Store.models import Product,ProductImage,ProductCategory

# Register your models here.
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductCategory)