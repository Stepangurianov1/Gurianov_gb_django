from django.shortcuts import render

# Create your views here.

def index(request):
    coontex = {
        'button':['Начать покупки', 'Каталог', 'Войти', 'User', 'Выйти'],
        'title':'GeekShop',
        'text':['Новые образы и лучшие бренды на GeekShop Store. Бесплатная доставка по всему миру! Аутлет: до -70% Собственный бренд. -20% новым покупателям.','geekShop Store']
    }
    return render(request,'index.html', coontex)

def products(request):
    context = {

    'title':['Отправить в корзину','Удалить из корзины', 'GeekShop - Каталог'],
    'menu':['Новинки','Одежда','Обувь','Аксесуары','Подарки'],
    'products':[
        {'name': 'Худи черного цвета с монограммами adidas Originals','price':'6 090,00 руб.','title':'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.'},
        {'name': 'Синяя куртка The North Face', 'price': '23 725,00 руб.','title': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.'},
        {'name': 'Коричневый спортивный oversized-топ ASOS DESIGN', 'price': '3 390,00 руб.', 'title': 'Материал с плюшевой текстурой. Удобный и мягкий.'},
        {'name': 'Черный рюкзак Nike Heritage', 'price': '2 340,00 руб.', 'title': 'Плотная ткань. Легкий материал.'},
        {'name': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex', 'price': '13 590,00 руб.', 'title': 'Гладкий кожаный верх. Натуральный материал.'},
        {'name': 'Темно-синие широкие строгие брюки ASOS DESIGN', 'price': '2 890,00 руб.', 'title': 'Легкая эластичная ткань сирсакер Фактурная ткань'},
    ]
    }
    print(context['products'][1]['name'])
    return render(request,'products.html',context)

