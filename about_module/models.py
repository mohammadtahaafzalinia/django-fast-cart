from django.db import models
from user_module.models import User
# Create your models here.


class AboutDelivery(models.Model):
    text = models.CharField(max_length=500,verbose_name='متن')
    icon = models.ImageField(upload_to='about/delivery',verbose_name='ایکون')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'جزئیات تحویل'
        verbose_name_plural = 'جزئیات تحویل'


class CustomerTurst(models.Model):
    title = models.CharField(max_length=60,verbose_name='موضوع')
    text = models.CharField(max_length=700,verbose_name='متن')
    text_shadow = models.CharField(max_length=6,help_text='نوشته سایه مانند در گوشه سمت چپ کارت ها',verbose_name='راهنمایی')
    icon = models.ImageField(upload_to='about/customer',verbose_name='ایکون')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'اعتماد مشتری'
        verbose_name_plural = 'اعتماد مشتریان'


class AboutUs(models.Model):
    title = models.CharField(max_length=300,verbose_name='موضوع')
    description = models.TextField(verbose_name='توضیحات')
    delivery_detail = models.ManyToManyField(AboutDelivery,verbose_name='جزئیات تحویل')
    image1 = models.ImageField(upload_to='about/main',verbose_name='عکس اول')
    image2 = models.ImageField(upload_to='about/main',verbose_name='عکس دوم')
    customer_turst = models.ManyToManyField(CustomerTurst,verbose_name='اعتماد مشتریان')
    maker = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='سازنده')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'درباره ما'
        verbose_name_plural = 'درباره ما'
