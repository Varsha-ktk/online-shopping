from django import forms
from django.contrib.auth.forms import UserCreationForm

from e_app.models import Login_view, Customer, Seller, Product


class LoginForm(UserCreationForm):

    class Meta:
        model = Login_view
        fields = ('username','password1','password2')


class CustomerForm(forms.ModelForm):
    class Meta:
        model=Customer
        fields = '__all__'
        exclude = ('user','status1')

class SellerForm(forms.ModelForm):
    class Meta:
        model=Seller
        fields = '__all__'
        exclude = ('user',)

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ('user',)



