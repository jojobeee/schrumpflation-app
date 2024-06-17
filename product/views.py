from django.shortcuts import render
from .models import Product, Purchase

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, 'product/index.html', context)

def productDetail(request, product_id):
    product = Product.objects.get(id=product_id)
    purchases = Purchase.objects.filter(product=product)
    context = {'product': product,'purchases': purchases,}
    return render(request, 'product/productDetail.html', context)