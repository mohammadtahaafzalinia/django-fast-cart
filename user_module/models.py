import uuid
from django.utils.crypto import get_random_string
from django.db import models
from django.contrib.auth.models import AbstractUser
from jalali_date import *
import secrets
# Create your models here.
from products_module.models import Product

code_unique=secrets.token_urlsafe(8)[:10]
uuid_list = [uuid.uuid4()]


class User(AbstractUser):
    avatar = models.ImageField(null=True,upload_to='user_module/%Y/%b',verbose_name='اواتار')
    email_code = models.CharField(null=True,max_length=100,verbose_name='کد فعالسازی')
    address = models.TextField(null=True,default='',verbose_name='ادرس')
    ip_user = models.GenericIPAddressField(null=True,verbose_name='ای پی کاربر')
    Disable_access = models.BooleanField(default=False,verbose_name='قطع کردن دسترسی کاربر')
    wallet = models.PositiveIntegerField(null=True,verbose_name='کیف پول')
    code_post = models.CharField(null=True,default='',blank=True,max_length=10,verbose_name='کدپستی')
    city_list = [['Sabzevar','سبزوار'],['Tehran','تهران'],['Karaj','کرج'],['Mashhad','مشهد'],['neyshabor','نیشابور'],['Yazd','یزد']]
    city = models.CharField(max_length=100,choices=city_list,default='سبزوار' ,verbose_name='شهر')
    phone = models.CharField(max_length=16,default='+98',verbose_name='تلفن همراه')
    gender_list = [['Woman','زن'],['man','مرد'],['unknown','نامشخص'],['dont_say','نمی خواهم بگویم']]
    gender = models.CharField(default=gender_list[2][1],max_length=50,choices=gender_list,verbose_name='جنسیت')
    code_user = models.CharField(max_length=20,default=uuid_list,verbose_name='کد کاربر')
    class Meta:
        verbose_name='کاربر'
        verbose_name_plural = 'کاربران'

    def __str__(self):
        return self.username

    def get_jalali_date(self):
        return date2jalali(self.date_joined).strftime('%d %b %Y')


class Favorites(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')


class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')
    text = models.TextField(verbose_name='متن')
    check_by_admin = models.BooleanField(default=False,verbose_name='تایید توسط ادمین')
    reply = models.ForeignKey('Comments',null=True,blank=True,on_delete=models.CASCADE,verbose_name='پاسخ')
    date = models.DateTimeField(auto_now_add=True,null=True,verbose_name='تاریخ')


    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'


class Compare(models.Model):
    product = models.ManyToManyField(Product,related_name='product_ol',verbose_name='محصولات')
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='کاربر')

    def __str__(self):
        return self.user.username + ':' + str(self.id)

    class Meta:
        verbose_name = 'مقایسه'
        verbose_name_plural = 'مقایسه ها'


class MostPopular(models.Model):
    user = models.GenericIPAddressField(verbose_name='کاربر')
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name='محصول')