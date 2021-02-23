from django.shortcuts import render
from .models import OrderItem
from .forms import CreateOrderForm
from cart.cart import Cart
from .tasks import order_created


def create_order(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            if cart.coupon:
                order.coupon = cart.coupon
                order.discount = cart.coupon.discount
            order.save()
            for item in cart:
                OrderItem.objects.create(order=order, product=item['product'], price=item['price'],
                                         quantity=item['quantity'])
            cart.clear_session()
            # launch a asynchronous task
            order_created.delay(order.id)
            return render(request, 'orders/created.html')
    else:
        form = CreateOrderForm()
    context = {'cart': cart, 'form': form}
    return render(request, 'orders/create.html', context)
