from django.db import models
from django.core.validators import MaxValueValidator
# Create your models here.
from googletrans import Translator
from jalali_date import *
import secrets
from colorfield.fields import ColorField


code_unique=secrets.token_urlsafe(8)[:10]


def trans(value):
    g = Translator().translate(value).text
    return g


class Product_categorys(models.Model):
    title = models.CharField(max_length=30,verbose_name='موضوع')
    url = models.CharField(max_length=30,verbose_name='نام در url',help_text='english name category')
    image_category = models.ImageField(upload_to='Product_category/%Y',null=True,blank=True,verbose_name='عکس دسته بندی')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Product_tags(models.Model):
    name_tage = models.CharField(max_length=30,verbose_name='نام تگ')
    url = models.CharField(max_length=30,null=True,verbose_name='نام در url')

    def __str__(self):
        return self.name_tage

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class Product(models.Model):
    product_name = models.CharField(max_length=30,verbose_name='نام محصول')
    image = models.ImageField(upload_to='product/%Y/%b', verbose_name='عکس')
    image_sub= models.ImageField(blank=True,null=True,upload_to='product/%Y/%b', verbose_name='عکس فرعی')
    image_sub2= models.ImageField(blank=True,null=True,upload_to='product/%Y/%b', verbose_name='عکس فرعی2')
    image_sub3= models.ImageField(blank=True,null=True,upload_to='product/%Y/%b', verbose_name='عکس فرعی 3')
    price = models.PositiveIntegerField(verbose_name='قیمت')
    discount = models.PositiveIntegerField(blank=True,default=1,null=True,verbose_name='تخفیف')
    weight = models.CharField(max_length=50,default='',null=True,blank=True,verbose_name='وزن')
    datetime = models.DateTimeField(auto_now_add=True,verbose_name='زمان اضافه شدن محصول')
    code_product = models.CharField(max_length=11,default=code_unique,unique=True,verbose_name='کد محصول')
    is_active = models.BooleanField(default=False,verbose_name='موجود بودن محصول')
    score = models.PositiveIntegerField(default=5,validators=[MaxValueValidator(5)],verbose_name='امتیاز')
    category = models.ForeignKey(Product_categorys,on_delete=models.CASCADE,verbose_name='دسته بندی')
    list_choice = [('400-500', '400 تا 500 گرم'), ('500-700', '500 تا 700 گرم'), ('700-1kg', '700 تا 1 کیلوگرم'),('120-150g(two boxes)', '120 تا 150 گرم دو بسته')]
    size_box = models.CharField(max_length=70, choices=list_choice, verbose_name='سایز جعبه')
    product_number = models.PositiveIntegerField(verbose_name='تعداد محصول')
    short_description = models.CharField(max_length=300,blank=True,null=True,verbose_name='توضیحات کوتاه')
    title_des = models.CharField(max_length=30, null=True, blank=True, verbose_name='موضوع توضیحات')
    description = models.TextField(verbose_name='توضیحات')
    image_description = models.ImageField(blank=True, upload_to='product/description/%b', verbose_name='عکس در توضیحات')
    slug = models.SlugField(unique=True, verbose_name='اسلاگ')
    is_delete = models.BooleanField(default=False, verbose_name='پاک شدن محصول')
    diet = models.BooleanField(default=False,verbose_name='رژیم غذایی')
    tage = models.ManyToManyField(Product_tags,verbose_name='تگ')
    view_product = models.PositiveIntegerField(null=True,blank=True,verbose_name='تعدا بازدید از محصول')
    sales = models.PositiveIntegerField(default=0,verbose_name='فروش')
    proposal = models.BooleanField(default=False,verbose_name='محصول پیشنهادی')
    color = ColorField(default='#FFFFFF')

    def discount_def (self):
        return self.discount / 100

    def price_after_discount(self):
        return int(self.price - (self.price * self.discount / 100))

    def price_discount(self):
        return (self.price) - (int(self.price - (self.price * self.discount / 100)))
    def __str__(self):
        return self.product_name

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def get_jalali_data(self):
        return date2jalali(self.datetime).strftime('%d %b %Y')

    def get_jalali_time(self):
        return datetime2jalali(self.datetime).strftime('%H:%M %p')

    def get_jalali_DateTime(self):
        return datetime2jalali(self.datetime).strftime('%Y/%b/%d -- %H:%M %p')





class Instructions(models.Model):
    instruction = models.CharField(max_length=100, verbose_name='دستور عمل')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول مورد نظر')

    def __str__(self):
        return self.product.product_name

    class Meta:
        verbose_name = 'دستور العمل'
        verbose_name_plural = 'دستور العمل ها'


class Product_features(models.Model):
    name_product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='محصول مورد نظر')
    name_feature = models.CharField(max_length=50,verbose_name='نام ویژگی')
    attribute_value = models.CharField(max_length=60,verbose_name='مقدار ویزگی')

    def __str__(self):
        return self.name_product.product_name

    class Meta:
        verbose_name = 'ویژگی محصول'
        verbose_name_plural = 'ویژگی محصولات'




