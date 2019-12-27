from django.shortcuts import render
from .models import Product
from .models import Category


def product_in_category(request, category_slug= None):
    current_category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available_display= True)

    if category_slug:
        current_category = get_objects_or_404(Category, slug=category_slug)  # 만약 객체가 존재하지 않을 때 get() 을 사용하여 Http404 예외를 발생
        products = products.filter(category=current_category)

    return render(request, 'shop/list.html',{'current_category':current_category,'categories':categories,'products':products})


def product_detail(request,id,product_slug= None):
    product = get_objects_or_404(Product,id=id, slug=product_slug)

    return render(request, 'shop/detail.html',{'product':product})
