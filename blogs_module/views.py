from django.shortcuts import render
from django.views.generic import *
from django.http import *
import blogs_module.models
from .models import *

# Create your views here.


class blogGrid(ListView):
    template_name = 'blog-grid.html'
    model = Blogs
    context_object_name = 'blogs'
    ordering = '-id'
    paginate_by = 12

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(blogGrid, self).get_context_data(**kwargs)
        tags = BlogTags.objects.all()
        categorys = BlogCategory.objects.all()
        blogNew = Blogs.objects.order_by('-date')[:4]
        blogView = Blogs.objects.order_by('-blog_view')
        blogMostPopular = blogView[0]
        blogViews = blogView[:3]
        x = 0.05
        for _ in range(6):
            x += 0.05
        context['data'] = x
        context['tags'] = tags
        context['categorys'] = categorys
        context['blog_news'] = blogNew
        context['blogViews'] = blogViews
        context['blogMostView'] = blogMostPopular.id
        return context

    def get_queryset(self):
        key = list(self.request.GET.keys())
        value = list(self.request.GET.values())
        if key and value is not None:
            key = key[0]
            value = value[0]
            if key == 'tage':
                blogs=Blogs.objects.filter(tage__tage=value)
                return blogs
            if key == 'category':
                blogs=Blogs.objects.filter(category__url=value)
                return blogs
            if key == 'search':
                blogs: Blogs = Blogs.objects.filter(name_blog=value)
                if list(blogs) == []:
                    blogs=Blogs.objects.filter(slug=value)
                    if list(blogs) == []:
                        blogs=Blogs.objects.filter(short_description=value)
                        return blogs
                    return blogs
                return blogs
            elif key != 'tage' and key != 'category' and key != 'search':
                blogs = Blogs.objects.all()
                return blogs
        if key == [] and value == []:
            blogs = Blogs.objects.all()
            return blogs


class blogDitail(DetailView):
    template_name = 'blog-detail.html'
    model = Blogs

    def get_context_data(self, **kwargs):
        context = super(blogDitail, self).get_context_data(**kwargs)
        query = self.request.COOKIES.get('UserAuth')
        if query is not None:
            blog_slug = (list((self.kwargs).values()))[0]
            user = User.objects.get(email=query)
            blog = Blogs.objects.get(slug=blog_slug)
            MostPopularBlogCheck = BlogMostPopular.objects.filter(user=user.ip_user, blog_id=blog.id).first()
            if MostPopularBlogCheck is None:
                MostPopularBlog = BlogMostPopular(user=user.ip_user,blog_id=blog.id)
                MostPopularBlog.save()
                if blog.blog_view is None:
                    blog.blog_view = 1
                    blog.save()
                else:
                    BlogView = blog.blog_view + 1
                    blog.blog_view = BlogView
                    blog.save()
        blog_tage = BlogTags.objects.all()
        more_detail = MoreDetail.objects.all().order_by('id')
        context['blog_tages'] = blog_tage
        context['mores']=more_detail
        return context




