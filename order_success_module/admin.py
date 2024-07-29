from django.contrib import admin
from order_success_module.models import *
# Register your models here.
admin.site.register(BasketBuyModel)
admin.site.register(CartModel)
admin.site.register(OrderSuccessModel)