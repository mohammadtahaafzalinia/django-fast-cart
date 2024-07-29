from django.shortcuts import *
from .models import *
from django.views.generic import *
# Create your views here.


class OrderSuccessView(ListView):
    template_name = 'cart.html'
    model = BasketBuyModel

    def render_to_response(self, context, **response_kwargs):
        user_email = self.request.COOKIES.get('UserAuth')
        if user_email is None:
            return redirect('login_acount')
        else:
            user: User = User.objects.filter(email=user_email).first()
            if user is None:
                return redirect('login_acount')
            else:
                pass

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderSuccessView,self).get_context_data(**kwargs)
        user_email = self.request.COOKIES.get('UserAuth')
        if user_email is None:
            return redirect('login_acount')
        user: User = User.objects.filter(email=user_email).first()
        if user is None:
            return redirect('login_acount')
        cart = CartModel.objects.filter(user_id=user.id).first()
        if cart is None:
            context['not_cart'] = True
        else:
            baskets = BasketBuyModel.objects.filter(user_id=user.id, sale=False)
            if baskets.count() == 0:
                context['not_cart'] = True
                context['total_sum'] = cart.total_sum
                return context
            else:
                context['carts'] = baskets
                context['not_cart'] = False
                context['total_sum'] = cart.total_sum
                return context



def AddProductBasketBuy(request):
    product_id = request.GET.get('product_id')
    product = Product.objects.get(id=product_id)
    user_email = request.COOKIES.get('UserAuth')
    user : User = User.objects.filter(email=user_email).first()
    if user is None:
        return redirect('login_acount')
    else:
        if product_id is not None:
            checkBasket = BasketBuyModel.objects.filter(product_id=product_id,sale=False).first()
            if checkBasket is None:
                BasketBuyModel(product_id=product_id,number_product=1,user_id=user.id,total=product.price_after_discount()).save()
                basket_new = BasketBuyModel.objects.get(product_id=product_id,number_product=1,user_id=user.id)
                if CartModel.objects.filter(user_id=user.id).first() is None:
                    basket = CartModel.objects.create(user_id=user.id)
                    basket.cart.add(basket_new)
                    basket.total_sum = int(basket_new.product.price_after_discount())
                    basket.save()
                else:
                    basket = CartModel.objects.get(user_id=user.id)
                    basket.cart.add(basket_new)
                    basket.total_sum += int(basket_new.product.price_after_discount())
                    basket.save()
                return render(request,'cart.html')
        else:
            return redirect("main_product")


def TotalAndNumberProduct(request):
    minus = request.GET.get('minus')
    plus = request.GET.get('plus')
    product = request.GET.get('product')
    hi = request.GET.get('hi')
    number = int(plus) - int(minus)
    user_email = request.COOKIES.get('UserAuth')
    user : User = User.objects.filter(email=user_email).first()
    basketBuy : BasketBuyModel = BasketBuyModel.objects.filter(user_id=user.id,product_id=product).first()
    basket = CartModel.objects.get(user_id=user.id)
    if plus and minus is not None:
        # number product
        if hi == 'p':
            x = basketBuy.number_product + number
            basketBuy.number_product = x
            basketBuy.save()
            # total price in basket buy
            total_price = basketBuy.product.price_after_discount() * basketBuy.number_product
            basketBuy.total = total_price
            basketBuy.save()
            # cart
            y = basketBuy.number_product - 1
            total_sum = basketBuy.product.price_after_discount() * y
            basket.total_sum -= total_sum
            basket.total_sum += total_price
            basket.save()
        elif hi == 'm':
            x = basketBuy.number_product + number
            basketBuy.number_product = x
            basketBuy.save()
            # total price in basket buy
            total_price = basketBuy.product.price_after_discount() * basketBuy.number_product
            basketBuy.total = total_price
            basketBuy.save()
            # cart
            y = basketBuy.number_product - 1
            total_sum = basketBuy.product.price_after_discount() * y
            basket.total_sum += total_sum
            basket.total_sum -= total_price
            basket.save()
        return render(request,'TotalAndNumber.html')
    else:
        return redirect("Cart")


def DeleteCartView(request):
    basket_id = request.GET.get('basket_id')
    user_email = request.COOKIES.get('UserAuth')
    user : User = User.objects.filter(email=user_email).first()
    basket: BasketBuyModel = BasketBuyModel.objects.filter(id=basket_id,sale=False).first()
    if basket is not None:
        cart = CartModel.objects.get(user_id=user.id)
        total_sum = cart.total_sum - basket.total
        cart.total_sum = total_sum
        cart.cart.remove(basket)
        cart.save()
        if BasketBuyModel.objects.count() == 1:
            basket.delete()
            cart.delete()
        elif BasketBuyModel.objects.count() > 1:
            basket.delete()
    else:
        return redirect("Cart")
    return redirect("Cart")


class OrderSuccess(ListView):
    template_name = 'order-success.html'
    model = BasketBuyModel

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(OrderSuccess,self).get_context_data(**kwargs)
        user_email = self.request.COOKIES.get('UserAuth')
        user : User = User.objects.get(email=user_email)
        if user is None:
            return redirect('login_acount')
        basket = BasketBuyModel.objects.filter(user_id=user.id)
        cart_model = CartModel.objects.get(user_id=user.id)
        list_int = 0
        for item in basket:
            item.product.product_number -= item.number_product
            item.product.sales += item.number_product
            item.sale = True
            cart = item
            list_int += item.number_product
            item.product.save()
            item.save()
            if item.sale == False:
                item.delete()
        OrderSuccessModel(cart_id=cart_model.id,user_id=user.id,total_sum=cart_model.total_sum,product_number=list_int).save()
        context['carts'] = basket
        context['total_sum'] = cart_model.total_sum
        context['cart_item'] = cart
        return context




