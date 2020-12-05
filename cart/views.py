from django.shortcuts import render, redirect, get_object_or_404
# from django.views.decorators.http import require_POST
import json
from django.http import JsonResponse
from shop.models import Product
from .cart import Cart


def cart_add(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['productId']
        # action = data['action']
        # quantity = data['quantity']
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        cart.add(product=product, quantity=3)
        return JsonResponse({'status': 'ok'})


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})


def cart_remove(request):
    data = json.loads(request.body)
    product_id = data['productId']
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    # print(cart.get_total_price())
    return JsonResponse({'status': 'ok'})
