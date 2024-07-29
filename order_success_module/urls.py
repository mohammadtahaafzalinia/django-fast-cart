from django.urls import path
from .views import *

# Create your urls here.

urlpatterns = [
    path('',OrderSuccessView.as_view(),name='Cart'),
    path('success/',OrderSuccess.as_view(),name='order-success'),
    path('add-product-basketbuy/',AddProductBasketBuy,name='AddProductBasketBuy'),
    path('total-number-product/',TotalAndNumberProduct,name='TotalAndNumberProduct'),
    path('delete-basket/',DeleteCartView,name='delete-basket'),
]