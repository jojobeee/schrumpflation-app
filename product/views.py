from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def index(request):
    product_list = Product.objects.all()
    context = {'product_list': product_list}
    return render(request, 'product/index.html', context)

def item(request, item_id):
    return HttpResponse(f"You're looking at product {item_id}.")