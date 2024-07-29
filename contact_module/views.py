from django.shortcuts import *
from django.views.generic import CreateView
from .models import *
from .forms import *
from user_module.models import User
# Create your views here.


class ContactView(CreateView):
    template_name = 'contact-us.html'
    model = ContactUs
    form_class = ContactForm
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)
        contact_details = ContactDetails.objects.all()
        cookie_email = self.request.COOKIES.get('UserAuth')
        user = User.objects.filter(email=cookie_email).first()
        if user is not None:
            context['email'] = user.email
        elif user is None:
            context['email'] = False
        for item in contact_details:
            contact_detail = item
        context['contact']= contact_detail
        context['form'] = ContactForm
        return context

    def form_valid(self, form):
        cookie_email = self.request.COOKIES.get('UserAuth')
        form_class = ContactForm(self.request.POST)
        if form_class.is_valid():
            if cookie_email is None:
                return redirect('sign-up')
            elif cookie_email is not None:
                user = User.objects.filter(email=cookie_email).first()
                text = form_class.cleaned_data.get('text')
                ContactUs(text=text,user_id=user.id,email=user.email).save()
                return redirect('home')
        return super().form_valid(form)
