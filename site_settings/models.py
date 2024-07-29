from django.db import models

# Create your models here.


class HomeSettings(models.Model):
    icon = models.ImageField(upload_to='home_images',verbose_name="ایکون")
    icon_phone = models.ImageField(upload_to='home_images',null=True,verbose_name="ایکون پشتیبانی")
    phone = models.CharField(max_length=100,verbose_name="شماره پشتیبانی")
    description = models.TextField(default='',blank=True,verbose_name="توضیحات")
    user_description = models.TextField(default='',blank=True,verbose_name="توضیحات در داشبورد کاربر")
    user_profile_description = models.TextField(default='',blank=True,verbose_name="توضیحات در داشبورد کاربر بخش پروفایل")
    address = models.CharField(max_length=100,default='',blank=True,verbose_name="ادرس")
    email = models.EmailField(null=True,verbose_name="ایمیل")
    twitter = models.URLField(max_length=100,default='',blank=True,verbose_name="توییتر")
    facebook = models.URLField(max_length=100,default='',blank=True,verbose_name="فیسبوک")
    instagram = models.URLField(max_length=100,default='',blank=True,verbose_name="اینستاگرام")
    pinterest = models.URLField(max_length=100,default='',blank=True,verbose_name="پینترست")
    link = models.URLField(max_length=100,default='',blank=True,verbose_name="لینک")

    def __str__(self):
        return 'تنظیمات صفحه خانه'

    class Meta:
        verbose_name = "تنظیمات سایت صفحه خانه"
        verbose_name_plural = "تنظیمات سایت صفحه خانه"
        constraints = [
            models.CheckConstraint(check=models.Q(id__lt=2),name="max_items_limit1")
        ]


class SiteSettingsHome(models.Model):
    image = models.ImageField(upload_to='home_images',verbose_name="عکس")
    description = models.TextField(default='',blank=True,verbose_name="توضیحات")
    short_description = models.CharField(max_length=100,blank=True,default='',verbose_name="توضیحات کوتاه")
    title = models.CharField(max_length=100,blank=True,default='',verbose_name="کلمات کلیدی")
    url = models.CharField(max_length=100,verbose_name="ادرس")

    def __str__(self):
        return f'تبلیغ شماره{self.pk}'

    class Meta:
        verbose_name = "تبلیغات صفحه خانه"
        verbose_name_plural = "تبلیغات صفحه خانه"
        constraints = [
            models.CheckConstraint(check=models.Q(id__lt=14),name="max_items_limit2")
        ]


class SiteSettings(models.Model):
    pages = (('product_list','product_list'),('product_details','product_details'))
    page = models.CharField(choices=pages, max_length=50,verbose_name="صفحه")
    image = models.ImageField(upload_to='product_images',verbose_name="عکس")
    description = models.TextField(default='',verbose_name="توضیحات")
    short_description = models.CharField(max_length=100,default='',verbose_name="توضیحات کوتاه")
    title = models.CharField(max_length=100,blank=True,default='',verbose_name="کلمات کلیدی")
    url = models.CharField(max_length=100,verbose_name="ادرس")

    def __str__(self):
       return self.page

    class Meta:
        verbose_name = "تنظیم سایت"
        verbose_name_plural = "تنضیمات سایت"
        constraints = [
            models.CheckConstraint(check=models.Q(id__lt=3),name="max_items_limit3")
        ]