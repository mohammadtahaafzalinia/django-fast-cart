import os
from order_success_module.models import *
from django.shortcuts import render,redirect,reverse
import random
from django.contrib.auth  import  get_user_model
from .forms import *
from django.views import View
from django.views.generic import *
from django.http import HttpRequest,Http404,JsonResponse,HttpResponse
from .models import *
from django.utils.crypto import get_random_string
from django.contrib.auth import login,logout
from utils.email_service import *
from site_settings.models import *
import logging

email_code_random = random.randint(10000,99999)


class otp(View):
    def get(self,request:HttpRequest):
        cookie_email = request.COOKIES.get('UserAuth')
        new_user = User.objects.filter(email=cookie_email).first()
        send_email_code(' کد فعالسازی', new_user.email, {'user': new_user}, 'email_active/welcome.html')
        return redirect(reverse('active'))

    def post(self,request:HttpRequest):
        cookie_email = request.COOKIES.get('UserAuth')
        new_user = User.objects.filter(email=cookie_email).first()
        form_class = Otp_form(request.POST)
        if form_class.is_valid():
            send_email_code(' کد فعالسازی', new_user.email, {'user': new_user}, 'email_active/welcome.html')
            return redirect(reverse('active'))
        return redirect(reverse('active'))


class SingUp(View):
    def get(self,request:HttpRequest):
        cookie = request.COOKIES.get('UserAuth')
        if cookie is None:
            accountView=account_form
            return render(request,'sign-up.html',{'account':accountView})
        elif cookie is not None:
            return redirect('user-dashboard')

    def post(self,request:HttpRequest):
        cookie = request.COOKIES.get('UserAuth')
        if cookie is None:
            accountView = account_form(request.POST)
            if accountView.is_valid():
                user_email = accountView.cleaned_data.get('email')
                user_name = accountView.cleaned_data.get('user_name')
                user_password = accountView.cleaned_data.get('password')
                ip_address= request.META['REMOTE_ADDR']
                user : bool =User.objects.filter(email__iexact=user_email,Disable_access=False).exists()
                if user:
                    accountView.add_error('email','مقادیر وارد شده درست نیست')
                else:
                    new_user = User(email=user_email,email_code=email_code_random,is_active=False,username=user_name,ip_user=ip_address)
                    new_user.set_password(user_password)
                    new_user.save()
                    cookie_email = HttpResponse('cookie user') and redirect(reverse('active'))
                    cookie_email.set_cookie('UserAuth',f'{new_user.email}',max_age=604800)
                    send_email_code(' کد فعالسازی',new_user.email,{'user':new_user},'email_active/welcome.html')
                    return cookie_email
            return render(request,'sign-up.html',{'account':accountView})
        elif cookie is not None:
            return redirect('user-dashboard')


class Login(View):

    def get(self,request):
        login_form = Login_form()
        cookie_user = request.COOKIES.get('UserAuth')
        user_cookie = User.objects.filter(email=cookie_user).first()
        return render(request,'log-in.html',{'login':login_form,'user':user_cookie})

    def post(self,request:HttpRequest):
        login_form=Login_form(request.POST)
        cookie_user = request.COOKIES.get('UserAuth')
        user_cookie = User.objects.filter(email=cookie_user).first()
        if login_form.is_valid():
            user_email = login_form.cleaned_data.get('email')
            if user_email == '2@2.com':
                login_form.password.error_messages.get('a')
            if cookie_user is None:
                cookie_user = HttpResponse('cookie user') and redirect('home')
                cookie_user.set_cookie('UserAuth', f'{user_email}',max_age=604800)
                return cookie_user
            user_password = login_form.cleaned_data.get('password')
            user : User = User.objects.filter(email__iexact=user_email,Disable_access=False).first()
            if user is not None :
                if not user.is_active:
                    login_form.add_error('email','حساب کاربری فعال نشده است')
                else:
                    password_cor = user.check_password(user_password)
                    if password_cor:
                        login(request,user)
                        return redirect(reverse('home'))
                    else:
                        login_form.add_error('password','رمز اشتباه است')
            else:
                login_form.add_error('email','حساب کاربری پیدا نشد')
        return render(request, 'log-in.html', {'login': login_form,'user':user_cookie})

d_login = []
class ActivateTheUser(View):
    def get(self,request:HttpRequest):
        form_class = Otp_form()
        cookie_user = request.COOKIES.get('UserAuth')
        if cookie_user is not None:
            user:User = User.objects.filter(email=cookie_user).first()
            if user is not None:
                return render(request, 'otp.html', {'form': form_class, 'user': user})
            else:
                return redirect('home')
        else:
            return redirect(reverse('sign-up'))

    def post(self,request:HttpRequest):
        form_class = Otp_form(request.POST)
        cookie_user = request.COOKIES.get('UserAuth')
        user_auth = User.objects.filter(email=cookie_user).first()
        if form_class.is_valid():
            code_form = form_class.cleaned_data.get('code')
            user: User = User.objects.filter(email_code=code_form).first()
            if user is not None:
                if not user.is_active:
                    user.is_active = True
                    user.save()
                    return redirect(reverse('login_acount'))
                else:
                    return redirect(reverse('login_acount'))
            return redirect(reverse('sign-up'))
        if cookie_user is not None:
            return render(request, 'otp.html', {'form': form_class, 'user': user_auth})
        elif cookie_user is None:
            return redirect(reverse('sign-up'))


class ForgetPassword(View):

    def get(self,request):
        forget_pass=Forget_pass_form()
        return render(request,'forgot.html',{'forget_pass':forget_pass})

    def post(self,request:HttpRequest):
        forget_pass=Forget_pass_form(request.POST)
        if forget_pass.is_valid():
            user_email = forget_pass.cleaned_data.get('email')
            user : User = User.objects.filter(email__iexact=user_email).first()
            if user is not None:
                send_email_code('فراموشی گذرواژه',user.email,{'user':user},'email_active/reset-password.html')
                return redirect(reverse('email_code'))
            else:
                return redirect(reverse('account'))
        return render(request,'forgot.html',{'forget_pass':forget_pass})


class ResetPassword(View):
    def get(self,request):
        username = request.COOKIES.get('UserAuth')
        uesr: User = User.objects.filter(email=username).first()
        if uesr is None:
            return redirect(reverse('login_acount'))
        reset_password = Rest_password()
        return render(request,'reset_pass.html',{'reset_pass':reset_password,'user':uesr})

    def post(self,request:HttpRequest):
        reset_password = Rest_password(request.POST)
        if reset_password.is_valid():
            password = reset_password.cleaned_data.get('password')
            re_password = reset_password.cleaned_data.get('re_password')
            username = request.COOKIES.get('UserAuth')
            user: User = User.objects.filter(email=username).first()
            if username is None:
                return redirect('login_acount')
            if username is not None:
                if user.check_password(password):
                    user.set_password(re_password)
                    user.save()
                    return redirect('user-dashboard')
                else:
                    reset_password.add_error('password','پسورد نادرست است')

        return render(request, 'reset_pass.html', {'reset_pass': reset_password})


def UserDashboard(request:HttpRequest):
    query = request.COOKIES.get('UserAuth')
    user = User.objects.filter(email=query).first()
    if user is None:
        return redirect(reverse('login_acount'))
    elif user is not None:
        x = 0
        orders = BasketBuyModel.objects.filter(user_id=user.id,sale=False)
        order_success = OrderSuccessModel.objects.filter(user_id=user.id)
        for item in order_success:
            x += item.product_number
        site = HomeSettings.objects.get(id=1)
        context = {
            'user': user,
            'site':site,
            'order_success':BasketBuyModel.objects.filter(user_id=user.id,sale=True),
            'basket_orders': orders,
            'favorite_count':Favorites.objects.filter(user_id=user.id).count(),
            'carts_count':orders.count(),
            'cart_total_count':x,
            'date_field': user.last_login.strftime("%Y - %m - %d"),
            'favorites':Favorites.objects.filter(user_id=user.id).order_by('-id')[:8]
        }
        return render(request,'user-dashboard.html',context)


def FavoriteView(request:HttpRequest):
    email = request.COOKIES.get('UserAuth')
    user = User.objects.filter(email=email).first()
    if user is None:
        return redirect('login_acount')
    elif user is not None:
        favorite = Favorites.objects.filter(user_id=user.id)
        return render(request,'wishlist.html',{'favorites':favorite})


def Privacy(request:HttpRequest):
    DeleteAccount = request.GET.get('DeleteAccount')
    Logout = request.GET.get('Logout')
    email = request.COOKIES.get('UserAuth')
    user: User = User.objects.filter(email=email).first()
    # automatic delete account
    if DeleteAccount == 'True':
        response = HttpResponse("delete account") and redirect('home')
        response.delete_cookie('UserAuth')
        user.delete()
        return response
    if Logout == 'True':
        response = HttpResponse("delete account") and redirect('home')
        response.delete_cookie('UserAuth')
        return response
    return render(request,'DeleteAccount.html')


def EditProfile(request:HttpRequest):
    username = request.GET.get('username')
    email = request.GET.get('email')
    city = request.GET.get('city')
    phone = request.GET.get('phone')
    address = request.GET.get('address')
    code_post = request.GET.get('code_post')
    user_email = request.COOKIES.get('UserAuth')
    if user_email is None:
        return redirect('login_acount')
    else:
        user: User = User.objects.filter(email=user_email).first()
        user.username = username
        user.email = user_email
        user.city = city
        user.phone = phone
        user.address = address
        user.code_post = code_post
        user.save()
        return render(request,'EditProfile.html')


