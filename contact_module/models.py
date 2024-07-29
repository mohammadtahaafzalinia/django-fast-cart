from django.db import models
from user_module.models import User
# Create your models here.


class ContactDetails(models.Model):
    phone = models.PositiveIntegerField(verbose_name='شماره تلفن')
    address = models.CharField(max_length=300,verbose_name='ادرس')
    email = models.EmailField(verbose_name='ایمیل')

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'مشخصات تماس با ما'
        verbose_name_plural = 'مشخصات تماس با ما'


class ContactUs(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,verbose_name='کاربر')
    text = models.TextField(verbose_name='متن')
    email = models.EmailField(null=True,blank=True,verbose_name='ایمیل')
    read_by_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'تماس با ما'
        verbose_name_plural = 'تماس با ما'