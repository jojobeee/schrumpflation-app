from django.shortcuts import render
from .models import Product, Purchase
from django.db.models import Q
from django.core.paginator import Paginator

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

    paginator = Paginator(product_list, 10)
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
