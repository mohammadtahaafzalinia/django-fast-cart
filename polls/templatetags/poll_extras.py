import datetime
from jalali_date import *
from django import template
from user_module.models import Comments
from site_settings.models import *
from products_module.models import *
register = template.Library()

list_category_id = []
for item in Product_categorys.objects.all():
    list_category_id.append(item.id)


@register.filter
def filter_model_1(value):
    return value.filter(category_id=list_category_id[0])

@register.filter
def filter_model_2(value):
    return value.filter(category_id=list_category_id[1])

@register.filter
def filter_model_3(value):
    return value.filter(category_id=list_category_id[2])

@register.filter
def order(value):
    return value[:4]

@register.filter
def order2(value):
    orders = []
    for item in value.order_by('sales'):
        if item.sales != 0:
            orders.append(item)
    return orders
@register.filter
def city(value):
    return value[0]


@register.filter
def city_en(value):
    return value[1]


@register.filter
def len_p(value):
    return range(len(value))


@register.filter
def activate_y(value):
    date = datetime.datetime.now().year
    total = int(date - value)
    if total > 0:
        return f'{total}سال'
    elif total < 0:
        return f''


@register.filter
def activate_m(value):
    date = datetime.datetime.now().month
    total = int(date - value)
    if total > 0:
        return f'/{total}ماه'
    elif total < 0:
        return f''

@register.filter
def activate_d(value):
    date = datetime.datetime.now().day
    total = int(date - value)
    if total > 0:
        return f'/{total}روز'
    elif total < 0:
        return f''


@register.filter
def jalaliDate(value):
    return date2jalali(value).strftime('%Y/%m/%d')


@register.filter
def jalaliTime(value):
    return datetime2jalali(value).strftime('%p %M:%H')

@register.filter
def rangeInt(value):
    return range(value)

@register.filter
def rangeNotfill(value):
    return range(5 - value)

@register.filter
def comments(value):
    comment : Comments = Comments.objects.filter(product_id=value,check_by_admin=True).count()
    return comment

@register.filter
def title_m(value):
    return SiteSettingsHome.objects.get(id=value).title

@register.filter
def image_m(value):
    return SiteSettingsHome.objects.get(id=value).image.url

@register.filter
def description_m(value):
    return SiteSettingsHome.objects.get(id=value).description


@register.filter
def short_description_m(value):
    return SiteSettingsHome.objects.get(id=value).short_description

@register.filter
def url_m(value):
    return SiteSettingsHome.objects.get(id=value).url

# 2
@register.filter
def title_s(value):
    return SiteSettings.objects.get(id=value).title

@register.filter
def image_s(value):
    return SiteSettings.objects.get(id=value).image.url

@register.filter
def description_s(value):
    return SiteSettings.objects.get(id=value).description


@register.filter
def short_description_s(value):
    return SiteSettings.objects.get(id=value).short_description

@register.filter
def url_s(value):
    return SiteSettings.objects.get(id=value).url