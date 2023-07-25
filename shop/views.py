from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
# Create your views here.


def index(request):
    return render(request, 'index.html')


def collection(request):
    # catprods=Product.objects.values('category')
    # cats={item['category'] for item in catprods}
    # print(cats)
    # for cat in cats:
    #     prod=Product.objects.filter(category=cat)
    products = Product.objects.all().filter(is_available='True')
    products_count=products.count()
    context = {
        'products': products,
        'products_count':products_count,
        }
    return render(request, 'collection.html',context)
def kurti(request):
        products = Product.objects.all().filter(category='kurti',is_available='True')
        products_count=products.count()
        context = {
        'products': products,
        'products_count':products_count,
        }
        return render(request, 'collection.html',context)
