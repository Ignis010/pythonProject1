from django.shortcuts import render, get_object_or_404
from .models import Category, Product

# Create your views here.

def aboutRender(request):
    return render(request, 'main/about.html')

def blogRender(request):
    return render(request, 'main/blog.html')

def cartRender(request):
    return render(request, 'main/cart.html')

def checkoutRender(request):
    return render(request, 'main/checkout.html')

def confirmationRender(request):
    return render(request, 'main/confirmation.html')

def contactRender(request):
    return render(request, 'main/contact.html')

def indexRender(request):
    return render(request, 'main/index.html')

def loginRender(request):
    return render(request, 'main/login.html')

def productlistRender(request, category_slug = None):
    category = None
    categories = Category.object.all()
    products = Product.object.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'main/product_list.html',
                  {
                      'category': category,
                      'categories': categories,
                      'products': products
                  })

def singleblogRender(request):
    return render(request, 'main/single-blog.html')

def singleproductRender(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)

    return render(request, 'main/single-product.html',
                  {
                      'product':product
                  })


