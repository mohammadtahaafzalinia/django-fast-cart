from django.db import models
from products_module.models import Product
from user_module.models import User
# Create your models here.


class BasketBuyModel(models.Model):
    product = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="محصول")
    total = models.PositiveIntegerField(null=True,blank=True,verbose_name="قیمت کل")
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    number_product = models.PositiveIntegerField(null=True,blank=True,verbose_name="تعداد محصول")
    sale = models.BooleanField(default=False,verbose_name="پرداخت شده")


class CartModel(models.Model):
    cart = models.ManyToManyField(BasketBuyModel,verbose_name="سبد خرید")
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    total_sum = models.PositiveIntegerField(null=True,blank=True,verbose_name="جمع نهایی")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "سبد خرید"
        verbose_name_plural = "سبد خرید"


class OrderSuccessModel(models.Model):
    cart = models.ForeignKey(CartModel,on_delete=models.CASCADE,verbose_name="سبد خرید")
    user = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name="کاربر")
    total_sum = models.PositiveIntegerField(null=True,blank=True,verbose_name="جمع نهایی")
    product_number = models.PositiveIntegerField(null=True,blank=True,verbose_name="تعداد محصولات خریداری شده")
    date_added = models.DateTimeField(auto_now_add=True,verbose_name="تاریخ")

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = "سبد خرید موفق"
        verbose_name_plural = "سبد خرید موفق"
