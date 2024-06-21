from django.shortcuts import render, redirect
from .models import Product, Purchase
from django.db.models import Q
from django.core.paginator import Paginator
from .forms import PurchaseForm, ProductForm
from .models import Product

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    purchases = Purchase.objects.filter(product=product)
    context = {'product': product,'purchases': purchases,}
    return render(request, 'product/productDetail.html', context)

def product_list(request):
    search_query = request.GET.get('search', '')
    brand_filter = request.GET.get('brand', '')
    product_type_filter = request.GET.get('product_type', '')

    if search_query:
        product_list = Product.objects.filter(
            Q(name__icontains=search_query) | 
            Q(brand__name__icontains=search_query) |
            Q(product_type__icontains=search_query)
        )
    else:
        product_list = Product.objects.all()

    if brand_filter:
        product_list = product_list.filter(brand__name__icontains=brand_filter)

    if product_type_filter:
        product_list = product_list.filter(product_type__icontains=product_type_filter)

    product_list = product_list.order_by('id')

    paginator = Paginator(product_list, 8)
    page_number = request.GET.get('page')
    products = paginator.get_page(page_number)

    brands = Product.objects.filter(
        Q(name__icontains=search_query) | 
        Q(brand__name__icontains=search_query) |
        Q(product_type__icontains=search_query)
    ).values_list('brand__name', flat=True).distinct()

    product_types = Product.objects.filter(
        Q(name__icontains=search_query) | 
        Q(brand__name__icontains=search_query) |
        Q(product_type__icontains=search_query)
    ).values_list('product_type', flat=True).distinct()

    return render(request, 'product/index.html', {
        'products': products,
        'brands': brands,
        'product_types': product_types,
        'selected_brand': brand_filter,
        'selected_product_type': product_type_filter,
        'search_query': search_query
    })

def add_purchase(request):
    product_form = ProductForm()
    purchase_form = PurchaseForm()
    if request.method == 'POST':
        if product_form.is_valid() and purchase_form.is_valid():
            product = product_form.save()
            purchase = purchase_form.save(commit=False)
            purchase.product = product
            purchase.save()
            return redirect('product:index') 
        
    return render(request, 'product/add_purchase.html', {'product_form': product_form, 'purchase_form': purchase_form})