from django.shortcuts import render
from django.views.generic import *
from .models import *
from blogs_module.models import Blogs
# Create your views here.


class AboutView(ListView):
    template_name = 'about-us.html'
    model = AboutUs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        about = AboutUs.objects.all()
        blogNew = Blogs.objects.order_by('-date')[:5]
        for item in about:
            item_about = item
        deilvery = AboutDelivery.objects.all()
        customerTurst = CustomerTurst.objects.all()
        context['about'] = item_about
        context['deilverys'] = deilvery
        context['customers'] = customerTurst
        context['blog_news'] = blogNew
        return context
