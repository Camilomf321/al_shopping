from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
from coupons.forms import CouponForm
import json
from django.http import JsonResponse
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm


def cart_add(request, product_id):
    # data = json.loads(request.body)
    # product_id = data['productId']
    if request.method == 'POST':
        # action = data['action']
        # quantity = data['quantity']

        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product, quantity=cd['quantity'], update_quantity=cd['update'])
        # return JsonResponse({'status': 'ok'})
        return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(
            initial={'quantity': item['quantity'],
                     'update': True})

    coupon_apply_form = CouponForm()
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'coupon_apply_form': coupon_apply_form})


def cart_remove(request):
    data = json.loads(request.body)
    product_id = data['productId']
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    # print(cart.get_total_price())
    return JsonResponse({'status': 'ok'})
