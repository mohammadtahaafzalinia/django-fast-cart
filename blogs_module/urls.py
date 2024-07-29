from django.urls import path
from blogs_module.views import *

urlpatterns = [
    path('',blogGrid.as_view(),name='blog-grid'),
    path('<slug:slug>/',blogDitail.as_view(),name='blog-ditail'),
    # path('<slug:slug>/',blogDitail.as_view(),name='blog-filter'),
]