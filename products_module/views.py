from django.shortcuts import render,redirect
from django.views.generic import *
from django.http import HttpRequest, JsonResponse
from django_filters.views import FilterView
from .filters import *
from user_module.models import *
from site_settings.models import *

# Create your views here.


class ProductList(FilterView):
    template_name = 'shop-right-sidebar.html'
    model = Product
    context_object_name = 'products'
    filterset_class = ProductFilter

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductList, self).get_context_data(**kwargs)
        query = self.request.COOKIES.get('UserAuth')
        price_filter = self.request.GET.get('price_filter')
        discount_filter = self.request.GET.get('discount_filter')
        score_filter = self.request.GET.get('score_filter')
        mostPopular = self.request.GET.get('mostPopular')
        warning = self.request.GET.get('warning')
        site_setting = SiteSettings.objects.all()
        #user
        product_id = []
        if query is not None:
            user = User.objects.filter(email=query).first()
            if user is not None:
                favorite = Favorites.objects.filter(user_id=user.id)
                for item in favorite:
                    product_id.append(item.product_id)
                context['product_id'] = product_id
                context['user'] = user
            else:
                context['user'] = None
        #price_filter
        if price_filter and discount_filter and score_filter and mostPopular is None:
            filters = self.filterset_class(self.request.GET,queryset=self.get_queryset())
            context['products'] = filters.qs
        else:
            if price_filter == "low":
                context['products'] = Product.objects.all().order_by("price")
                context['base_ordering'] = 'کمترین قیمت'
            elif price_filter == "high":
                context['products'] = Product.objects.all().order_by("-price")
                context['base_ordering'] = 'بیشترین قیمت'
            # discount_filter
            if discount_filter == "high":
                context['products'] = Product.objects.all().order_by("-discount")
                context['base_ordering'] = 'بیشترین تخفیف'
            # score_filter
            if score_filter == "high":
                context['products'] = Product.objects.all().order_by("-score")
                context['base_ordering'] = 'امتیاز'
            # most popular
            if mostPopular == "high":
                context['products'] = Product.objects.all().order_by("-view_product")
                context['base_ordering'] = 'محبوبترین'
        #context
        context['star'] = Product.objects.all()
        context['warning'] = warning
        context['site_settings'] = site_setting
        return context


class ProductDitail(DetailView):
    template_name = 'product-right-thumbnail.html'
    model = Product

    def get_context_data(self, **kwargs):
        contaxt = super(ProductDitail, self).get_context_data(**kwargs)
        query = self.request.COOKIES.get('UserAuth')
        site_setting = SiteSettings.objects.all()
        mostPopular = Product.objects.all().order_by("-view_product")[:3]
        if query is not None:
            product_slug = (list((self.kwargs).values()))[0]
            user = User.objects.get(email=query)
            product = Product.objects.get(slug=product_slug)
            MostPopularProductCheck = MostPopular.objects.filter(user=user.ip_user, product=product.id).first()
            if MostPopularProductCheck is None:
                MostPopularProduct = MostPopular(user=user.ip_user,product_id=product.id)
                MostPopularProduct.save()
                if product.view_product is None:
                    product.view_product = 1
                    product.save()
                else:
                    ProductView = product.view_product + 1
                    product.view_product = ProductView
                    product.save()
        instruction = Instructions.objects.all()
        tag= Product_tags.objects.all()
        features=Product_features.objects.all()
        products = Product.objects.all()
        url=list(self.kwargs.values())
        slug=url[0]
        product = Product.objects.filter(slug=slug).first()
        x = 0.05
        for _ in range(6):
            x += 0.05
        contaxt['data'] = x
        contaxt['most_poplars'] = mostPopular
        contaxt['site_settings'] = site_setting
        contaxt['tags']=tag
        contaxt['instructions']=instruction
        contaxt['features']=features
        contaxt['products']=products
        contaxt['stars']=range(int(product.score))
        contaxt['stars_null']=range(5-(int(product.score)))
        contaxt['comments']=Comments.objects.filter(product__slug=slug,check_by_admin=True)
        return contaxt


def favorite(request:HttpRequest):
    product_id = request.GET.get('jur75@4KDOUTDL[PWQIEYWK.BZN;A9YFEGFEIIY')
    email_cookie = request.COOKIES.get('UserAuth')
    user = User.objects.filter(email=email_cookie).first()
    if user is None:
        return redirect('login_acount')
    check_delete = Favorites.objects.filter(product_id=product_id,user_id=user.id).first()
    if product_id is not None:
        if check_delete is None:
            favorites = Favorites(product_id=product_id,user_id=user.id)
            favorites.save()
            return render(request,'AddDeleteFavorite.html')
        elif check_delete is not None:
            check_delete.delete()
            return render(request,'AddDeleteFavorite.html')
    elif product_id is None:
        return redirect('favorites')


def commentView(request:HttpRequest):
    comment = request.GET.get('comment')
    object_id = request.GET.get('object_id')
    reply_id = request.GET.get('reply_id')
    cookie = request.COOKIES.get('UserAuth')
    user = User.objects.filter(email=cookie).first()
    check_comment = list(Comments.objects.filter(text=comment,product_id=object_id,user_id=user.id))
    if check_comment == []:
        if user is not None:
            comments: Comments = Comments(text=comment, product_id=object_id, user_id=user.id, reply_id=reply_id)
            if comment and object_id is not None:
                comments.save()
            x= Comments.objects.filter(product_id=object_id,check_by_admin=True)
            return render(request, 'comment.html',{'comments':x})
        elif user is None:
            return redirect('login_acount')
    elif check_comment != []:
        return render(request,'comment.html',{'comments':Comments.objects.filter(product_id=object_id,check_by_admin=True)})


def CompareView(request):
    slug = request.GET.get('slug')
    cookie = request.COOKIES.get('UserAuth')
    warning = request.GET.get('warning')
    if cookie is not None:
        if slug is not None:
            product = Product.objects.get(slug=slug)
            user: User = User.objects.filter(email=cookie).first()
            check: Compare = Compare.objects.filter(user_id=user.id).first()
            if check is None:
                tabel = Compare.objects.create(user_id=user.id)
                tabel.product.add(product)
                tabel.save()
                product_ids = tabel.product.values("id")
                list_product_category = []
                for product_id in product_ids:
                    itme_product_list = list(product_id.values())[0]
                    list_product = Product.objects.get(id=itme_product_list)
                    list_product_category.append(list_product)
            check_item_product = list(check.product.values("id"))
            if check_item_product == []:
                check_item_product = None
            if check is not None and check_item_product is None:
                tabel = Compare.objects.get(user_id=user.id, id=check.id)
                tabel.product.add(product)
                tabel.save()
                product_ids = tabel.product.values("id")
                list_product_category = []
                for product_id in product_ids:
                    item_product_list = list(product_id.values())[0]
                    list_product = Product.objects.get(id=item_product_list)
                    list_product_category.append(list_product)
            elif check and check_item_product is not None:
                tabel = Compare.objects.get(user_id=user.id, id=check.id)
                compare_count = tabel.product.count()
                category_get_id = (list(list(set(tabel.product.values_list("category_id"))))[0])[0]
                if category_get_id == product.category_id:
                    if compare_count < 4:
                        tabel.product.add(product)
                        tabel.save()
                    elif compare_count == 4:
                        return redirect(f'/product/compare/?warning=TCBIF')
                    product_ids = tabel.product.values("id")
                    list_product_category = []
                    for product_id in product_ids:
                        itme_product_category = list(product_id.values())[0]
                        list_product = Product.objects.get(id=itme_product_category)
                        list_product_category.append(list_product)
                else:
                    return redirect(f'/product/?category={category_get_id}&warning=TCNS')
            return render(request, 'compare.html', {'products': list_product_category,'count': check.product.count(),'slug':True})
        else:
            user: User = User.objects.filter(email=cookie).first()
            check: Compare = Compare.objects.filter(user_id=user.id).first()
            if check.product.count() == 0:
                return redirect('main_product')
            return render(request, 'compare.html', {'products':check.product.all(),'count': check.product.count(),'warning':warning,'slug':False})

    elif cookie is None:
        return redirect('login_acount')


def DeleteProductCompare(request):
    cookie = request.COOKIES.get('UserAuth')
    user: User = User.objects.filter(email=cookie).first()
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)
    compare = Compare.objects.get(user_id=user.id)
    category_get_id = (list(list(set(compare.product.values_list("category_id"))))[0])[0]
    if compare.product.count() >= 2:
        compare.product.remove(product)
        return render(request, 'compareDelete.html', {'warning': False})
    elif compare.product.count() == 1:
        compare.product.remove(product)
        return render(request, 'compareDelete.html', {'Warning':True})


def SearchProducts(request):
    search = request.GET.get('search')
    if search is not None:
        product = Product.objects.filter(slug__iexact=search)
        if product.count() == 0:
            product = Product.objects.filter(product_name__iexact=search)
            if product.count() == 0:
                product = Product.objects.filter(short_description__iexact=search)
                if product.count() == 0:
                    return render(request,'search.html', {'not_found':True})
        return render(request,'search.html',{'products':product})
    elif search is None:
        product = Product.objects.all().order_by('-id')[:10]
        return render(request,'search.html',{'products':product})

