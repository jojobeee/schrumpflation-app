from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('product/<int:product_id>/', views.productDetail, name='productDetail'),
]
