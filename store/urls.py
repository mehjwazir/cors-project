from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    # path('', views.products_all, name='products_all'),
    path('about/', views.about, name='about'),
    path('base/', views.base, name='base'),
    path('about/', views.about, name='about'),
    path('product/<slug>/', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>/',
         views.category_list, name='category_list'),
]
