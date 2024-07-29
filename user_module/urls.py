from django.urls import path
from .views import *
urlpatterns = [
    path('',SingUp.as_view(),name='sign-up'),
    path('deleteAccount/',Privacy,name='deleteAccount'),
    path('editAccount/',EditProfile,name='editAccount'),
    path('login/',Login.as_view(),name='login_acount'),
    path('active-account/',ActivateTheUser.as_view(),name='active'),
    path('forget_password/',ForgetPassword.as_view(),name='forget_pass'),
    path('reset_password/',ResetPassword.as_view(),name='reset_password'),
    path('otp/',otp.as_view(),name='otp'),
    path('dashborad/',UserDashboard,name='user-dashboard'),
    path('favorites/',FavoriteView,name='favorites'),
]