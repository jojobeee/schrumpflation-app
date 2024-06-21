from django.urls import path
from . import views

app_name = 'product'
urlpatterns = [
    path('', views.product_list, name='index'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('product/add/', views.add_purchase, name='add'),
    path('autocomplete/products/', views.autocomplete_products, name='autocomplete_products'),
    path('product/details/', views.product_details, name='product_details'),
]
