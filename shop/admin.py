from django.contrib import admin
from shop.models import Product

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display=('product_name','category','brand','price','pub_date','is_available')
    
admin.site.register(Product,ProductAdmin)
