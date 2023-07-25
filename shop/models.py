from django.db import models

# Create your models here.
class Product(models.Model):
    product_name=models.CharField(max_length=50)
    category=models.CharField(max_length=50,default='')
    brand=models.CharField(max_length=50,default='')
    price=models.IntegerField()
    desc=models.CharField(max_length=400,default='')
    pub_date=models.DateField()
    image=models.ImageField(upload_to="shop/images",default='')
    is_available=models.BooleanField(default=True)

    def __str__(self):
        return self.product_name
