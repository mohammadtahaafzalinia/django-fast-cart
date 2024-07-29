from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(SiteSettings)
admin.site.register(SiteSettingsHome)
admin.site.register(HomeSettings)