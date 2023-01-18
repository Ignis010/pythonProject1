from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.indexRender, name='index'),

    path('about/', views.aboutRender, name='about'),

    path('cart/', views.cartRender, name='cart'),

    path('blog/', views.blogRender, name='blog'),

    path('checkout/', views.checkoutRender, name='checkout'),

    path('contact/', views.contactRender, name='contact'),

    path('confirmation/', views.confirmationRender, name='confirmation'),

    path('login/', views.loginRender, name='login'),

    path('product-list/', views.productlistRender, name='product_list'),

    path('single-product/', views.singleproductRender, name='single-product'),

    path('single-blog/', views.singleblogRender, name='single-blog')
]