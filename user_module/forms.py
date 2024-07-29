from django import forms
from django.core.validators import *
from django.http import HttpRequest
class account_form(forms.Form):
      user_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام کاربری'}),label='نام کاربری')
      email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),validators=[EmailValidator],label='ایمیل')
      password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}),label='رمز عبور')
      re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'تکرار رمز'}),label='تکرار رمز')

      def clean_confirm_password(self):
          password = self.cleaned_data.get('password')
          confirm_password = self.cleaned_data.get('confirm_password')
          if password == confirm_password:
                return confirm_password
          raise ValidationError('رمز عبور با تکرار رمز مطابقت ندارد')
class Login_form(forms.Form):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),validators=[EmailValidator])
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}))
class Forget_pass_form(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),validators=[EmailValidator])
class Rest_password(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمز عبور'}),label='رمز عبور')
    re_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'رمزعبور جدید'}),label='رمز عبور جدید')

class Otp_form(forms.Form):
    code = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'کد فعالسازی'}))