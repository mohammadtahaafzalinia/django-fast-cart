from django.contrib import admin
from .models import *
# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug':['name_blog']
    }


admin.site.register(Blogs, BlogAdmin)
admin.site.register(BlogCategory)
admin.site.register(BlogTags)
admin.site.register(MoreDetail)