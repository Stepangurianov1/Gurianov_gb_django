
from django.urls import path

from admins.views import index, admin_users_create, admin_users_delete, admin_users, category, \
    product, admin_product_create, admin_product_update, admin_product_delete, admin_users_update, \
    admin_category_create, admin_category_update

app_name = 'admins'
urlpatterns = [

    path('', index, name='index'),
    path('users/', admin_users, name='admin_users'),
    path('users-create/', admin_users_create, name='admin_users_create'),
    path('admin_product_create/', admin_product_create, name='admin_product_create'),
    path('users-update/<int:pk>', admin_users_update, name='admin_users_update'),
    path('admin_product_update/<int:pk>', admin_product_update, name='admin_product_update'),
    path('admin_category_update/<int:pk>', admin_category_update, name='admin_category_update'),
    path('admin_category_create/', admin_category_create, name='admin_category_create'),
    path('users-delete/<int:pk>', admin_users_delete, name='admin_users_delete'),
    path('admin_product_delete/<int:pk>', admin_product_delete, name='admin_product_delete'),
    path('category', category, name='category'),
    path('product', product, name='product'),
]
