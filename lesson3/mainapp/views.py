from django.shortcuts import render
import json
import os
from mainapp.models import Product, ProductCategory
MODULE_DIR = os.path.dirname(__file__)
def index(request):
    coontex = {
        'button':['Начать покупки', 'Каталог', 'Войти', 'User', 'Выйти'],
        'title':'GeekShop',
        'text':['Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.','geekShop Store']
    }
    return render(request,'index.html', coontex)

def products(request):
    context = {
    'title': ['Отправить в корзину','Удалить из корзины', 'GeekShop - Каталог'],
    }
    context['products'] = Product.objects.all()
    context['menu'] = ProductCategory.objects.all()
    return render(request,'products.html',context)

