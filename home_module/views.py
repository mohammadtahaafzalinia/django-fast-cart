from django.shortcuts import render
from django.views.generic import *
from products_module.models import *
from site_settings.models import *
from user_module.models import *
from order_success_module.models import *
from blogs_module.models import *
# Create your views here.


class home(ListView):
    template_name = 'home.html'
    model = Product
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(home, self).get_context_data(**kwargs)
        product = Product_categorys.objects.all()
        favorite = Favorites.objects.all().order_by('-id')[:1]
        user_email = self.request.COOKIES.get('UserAuth')
        user : User = User.objects.filter(email=user_email).first()
        sales = Product.objects.all().order_by('-sales')
        site_setting = HomeSettings.objects.all()
        blogs = Blogs.objects.all().order_by('-id')[:5]
        products = Product.objects.all()
        if site_setting.count() != 0:
            context['site_setting'] = site_setting.get(id=1)
            context['setting'] =True
        else:
            context['setting'] = False
        if user is None:
            context['message'] = False
        else:
            compare: Compare = Compare.objects.filter(user_id=user.id).first()
            basket = BasketBuyModel.objects.filter(user_id=user.id,sale=False)
            context['message'] = True
            if len(user.username) > 8:
                context['max_len'] = True
            else:
                context['max_len'] = False
            if compare is not None:
                context['compare_count'] = Compare.objects.get(user_id=user.id).product.count()
            else:
                context['compare_count'] = 0
            context['user'] = user
            context['basket_count'] = basket.count()
        for item in favorite:
            if favorite is not None:
                favorite_new = item
                context['favorite'] = favorite_new
            else:
                favorite_new = None
                context['favorite'] = favorite_new
        context['categorys'] = product
        context['rangs'] = range(5,9)
        context['sales'] = sales
        context['blogs'] = blogs
        context['products'] = products
        return context


def page_404(request):
    return render(request,'404.html')

def link(request):
    return render(request,'partial/link.html')


def footer(request):
    site = HomeSettings.objects.get(id=1)
    categorys = Product_categorys.objects.all()
    return render(request,'partial/footer.html',{"sites":site,'categorys':categorys})


def breadcrumb(request):
    return render(request,'partial/breadcrumb.html')


def js(request):
    return render(request,'partial/js.html')


def loader(request):
    return render(request,'partial/loader.html')


def modul_box(request):
    products = Product.objects.all().order_by('-sales')[:4]
    return render(request,'partial/modul_box.html',{'products':products})


def theme_options(request):
    return render(request,'partial/theme_options.html')


def mobile_fix(request):
    return render(request,'partial/mobile_fix.html')


def location_modul(request):
    return render(request,'partial/location_modul.html')


def header(request):
    category = Product_categorys.objects.all()
    user_email = request.COOKIES.get('UserAuth')
    site = HomeSettings.objects.get(id=1)
    if user_email is not None:
        user: User = User.objects.get(email=user_email)
        baskets = BasketBuyModel.objects.filter(user_id=user.id,sale=False)
        cart: CartModel = CartModel.objects.filter(user_id=user.id).first()
        if baskets.count() == 0:
            return render(request, 'partial/header.html', {'categorys': category, 'sites': site, 'context': False,'userauth':True})
        else:
            return render(request,'partial/header.html',{'user':user,'categorys':category,'carts':cart,'baskets':baskets,'sites':site,'context':True,'userauth':True})
    else:
        return render(request,'partial/header.html',{'categorys':category,'sites':site,'context':False,'userauth':False})