from django.contrib import admin
from .models import *
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':['product_name']
    }


admin.site.register(Product, ProductAdmin)
admin.site.register(Product_tags)
admin.site.register(Product_categorys)
admin.site.register(Product_features)
admin.site.register(Instructions)