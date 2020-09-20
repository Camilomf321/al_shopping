from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import JsonResponse
import json
from .models import Category, Product
# Create your views here.


def product_list(request):
    products = Product.product_available.all()
    categories = Category.objects.all()
    paginator = Paginator(products, 12)
    page_number = request.GET.get('page')
    page_products = paginator.get_page(page_number)
    context = {'products': page_products,
               'categories': categories,

               }
    return render(request, 'shop/product_list.html', context)


def product_detail(request, id, slug):
    product_item = get_object_or_404(Product, id=id, slug=slug, available=True)
    context = {'product_item': product_item}
    return render(request, 'shop/product_detail.html', context)

