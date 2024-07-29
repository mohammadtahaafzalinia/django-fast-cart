import uuid
from django.db import models
from user_module.models import User
from jalali_date import *
# Create your models here.
x=uuid.uuid4()


class BlogTags(models.Model):
    tage = models.CharField(max_length=50,verbose_name='تگ')

    def __str__(self):
        return self.tage

    class Meta:
        verbose_name = 'تگ'
        verbose_name_plural = 'تگ ها'


class BlogCategory(models.Model):
    name_category = models.CharField(max_length=50,verbose_name='نام دسته بندی')
    url = models.CharField(max_length=60,verbose_name='نام در url')

    def __str__(self):
        return self.name_category

    class Meta:
        verbose_name = 'دسته بندی'
        verbose_name_plural = 'دسته بندی ها'


class Blogs(models.Model):
    name_blog = models.CharField(max_length=60,verbose_name='نام بلاگ')
    image = models.ImageField(upload_to='Blogs/%Y',verbose_name='عکس')
    category = models.ForeignKey(BlogCategory,on_delete=models.CASCADE,verbose_name='دسته بندی')
    date = models.DateField(auto_now_add=True)
    short_description = models.CharField(max_length=100, verbose_name='توضیحات کوتاه')
    list_page_description = models.CharField(max_length=400,verbose_name='توضیحات در صفحه بلاگ لیست',null=True,blank=True)
    description = models.TextField(verbose_name='توضیحات')
    quote = models.CharField(max_length=300, verbose_name='نقل قول')
    author_quote = models.CharField(max_length=50, verbose_name='نویسنده نقل قول')
    author = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='نویسنده بلاگ')
    tage = models.ManyToManyField(BlogTags,verbose_name='تگ')
    is_active = models.BooleanField(default=False,verbose_name='فعال/غیرفعال')
    slug = models.SlugField(default="",unique=True,null=True,blank=True,verbose_name='اسلاگ')
    blog_view = models.PositiveIntegerField(null=True,blank=True,verbose_name='تعداد بازدید از بلاگ')
    def get_jalali_data(self):
        return date2jalali(self.date).strftime('%d %b %Y')

    def __str__(self):
        return self.name_blog

    class Meta:
        verbose_name = 'بلاگ'
        verbose_name_plural = 'بلاگ ها'


class MoreDetail(models.Model):
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE,null=True,verbose_name='بلاگ مورد نظر')
    description = models.TextField(verbose_name='توزیحات')

    def __str__(self):
        return self.blog.name_blog

    class Meta:
        verbose_name = 'توزیح'
        verbose_name_plural = 'توضیحات'


class CommentBlog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    blog = models.ForeignKey(Blogs,on_delete=models.CASCADE,verbose_name='بلاگ')
    text = models.TextField(verbose_name='متن')
    check_by_admin = models.BooleanField(default=False,verbose_name='تایید توسط ادمین')
    reply = models.ForeignKey('CommentBlog',null=True,blank=True,on_delete=models.CASCADE,verbose_name='پاسخ')
    date = models.DateTimeField(auto_now_add=True,null=True,verbose_name='تاریخ')

    def get_jalali_date(self):
        return date2jalali(self.date).strftime('%d %b %Y')

    def get_jalali_time(self):
        return datetime2jalali(self.date).strftime('%p %M:%H')

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'کامنت'
        verbose_name_plural = 'کامنت ها'


class BlogMostPopular(models.Model):
     user = models.GenericIPAddressField(verbose_name='ای پی کاربر')
     blog = models.ForeignKey(Blogs,on_delete=models.CASCADE,verbose_name='بلاگ')