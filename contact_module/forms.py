from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = ['text']
        widgets = {
            'text': forms.Textarea(
                attrs={'class': 'form-control', 'name': 'note', 'id': 'note', 'dir': 'rtl', 'placeholder': 'پیام خود را وارد کنید'})
        }