from django import forms
from django.contrib.auth.forms import UserCreationForm

from authapp.forms import UserRegisterForm, UserProfilerForm
from authapp.models import User
from mainapp.models import Product, ProductCategory


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'age', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(UserAdminRegisterForm, self).__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class UserAdminProfileForm(UserProfilerForm):
    email = forms.EmailField(widget=forms.EmailInput())
    username = forms.CharField(widget=forms.TextInput())

    def __init__(self, *args, **kwargs):
        super(UserAdminProfileForm, self).__init__(*args, **kwargs)

        self.fields['email'].widget.attrs['readonly'] = False
        self.fields['username'].widget.attrs['readonly'] = False
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
        self.fields['image'].widget.attrs['class'] = 'custom-file-input'


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'quantity', 'category')

    def __init__(self, *args, **kwargs):
        super(ProductCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название товара'
        self.fields['description'].widget.attrs['placeholder'] = 'Заполните описание'
        self.fields['price'].widget.attrs['placeholder'] = 'Заполните цену'
        self.fields['quantity'].widget.attrs['placeholder'] = 'Заполните колличество'
        self.fields['category'].widget.attrs['placeholder'] = 'Заполните категорию'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = ProductCategory
        fields = ('name', 'description')

    def __init__(self, *args, **kwargs):
        super(CategoryCreateForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = 'Введите название категории'
        self.fields['description'].widget.attrs['placeholder'] = 'Заполните описание'
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control py-4'
