from django.shortcuts import render
from shop.models import Category, Product


# Create your views here.
def home(request):
    latest_products = Product.product_available.all()[:6]  # últimos productos
    products_features = Product.product_featured.all()[:8]  # productos con descuentos
    context = {'latest_products': latest_products,
               'products_features': products_features
               }
    return render(request, 'home/home.html', context)


def contact(request):
    return render(request, 'home/contact.html')
