from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from admins.forms import UserAdminRegisterForm, UserAdminProfileForm, ProductCreateForm, CategoryCreateForm
from authapp.models import User
from mainapp.models import ProductCategory, Product


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'admins/admin.html')


@user_passes_test(lambda u: u.is_superuser)
def admin_users(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'admins/admin-users-read.html', context)


@user_passes_test(lambda u: u.is_superuser)
def category(request):
    context = {
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'admins/admin-category.html', context)


@user_passes_test(lambda u: u.is_superuser)
def product(request):
    context = {
        'products': Product.objects.all(),
    }
    return render(request, 'admins/admin-product.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return UserAdminProfileForm(reverse('admins:category'))
    else:
        form = UserAdminRegisterForm()
    context = {
        'title': 'Geekshop - Админ | Регистрация',
        'form': form
    }
    return render(request, 'admins/admin-users-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_create(request):
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:product'))
    else:
        form = ProductCreateForm()
    context = {
        'title': 'Geekshop - Админ | Продукты',
        'form': form
    }
    return render(request, 'admins/admin-product-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_create(request):
    if request.method == 'POST':
        form = CategoryCreateForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:category'))
    else:
        form = CategoryCreateForm()
    context = {
        'title': 'Geekshop - Админ | Категории',
        'form': form
    }
    return render(request, 'admins/admin-category-create.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_product_update(request, pk):
    product_select = Product.objects.get(pk=pk)
    if request.method == 'POST':
        form = ProductCreateForm(data=request.POST, instance=product_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:product'))
    else:
        form = ProductCreateForm(instance=product_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form': form,
        'product_select': product_select
    }
    return render(request, 'admins/admin-product-update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, pk):
    user_select = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, instance=user_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form': form,
        'user_select': user_select
    }
    return render(request, 'admins/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_category_update(request, pk):
    category_select = ProductCategory.objects.get(pk=pk)
    if request.method == 'POST':
        form = CategoryCreateForm(data=request.POST, instance=category_select, files=request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admins:category'))
    else:
        form = CategoryCreateForm(instance=category_select)
    context = {
        'title': 'Geekshop - Админ | Обновление',
        'form': form,
        'category_select': category_select
    }
    return render(request, 'admins/admin-category-update.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_delete(request, pk):
    if request.method == 'POST':
        user = User.objects.get(pk=pk)
        user.is_active = False
        user.save()

    return HttpResponseRedirect(reverse('admins:admin_users'))


@user_passes_test(lambda u: u.is_superuser)
def admin_product_delete(request, pk):
    if request.method == 'POST':
        product = Product.objects.get(pk=pk)
        product.delete()

    return HttpResponseRedirect(reverse('admins:product'))
