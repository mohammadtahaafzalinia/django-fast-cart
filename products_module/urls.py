from django.urls import path
from .views import *

urlpatterns = [
    path('add-favorite/',favorite, name='add-favorite'),
    path('delete/', DeleteProductCompare , name='compare-delete'),
    path('add-comment/',commentView, name='add-comment'),
    path('',ProductList.as_view(), name='main_product'),
    path('search/',SearchProducts, name='search_product'),
    path('compare/',CompareView, name='compare'),
    path('<slug:slug>/',ProductDitail.as_view(), name='ditail_product'),
]