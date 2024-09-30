from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from e_app.filter import NameFilter
from e_app.forms import BuyForm
from e_app.models import Customer, Product, Buy, Cart



@login_required(login_url='login_view')
def customer_productview(request):

    data = Product.objects.all()

    nameFilter = NameFilter(request.GET, queryset=data)
    data=nameFilter.qs
    return render(request, 'Customer/customer_productview.html', {'data': data,'nameFilter':nameFilter})

@login_required(login_url='login_view')
def buy_product(request,id):
    user = request.user
    obj = Customer.objects.get(user=user)
    data=Product.objects.get(id=id)
    count = request.POST.get("count")

    if request.method == 'POST':

        data1 = Buy()
        data1.product= data
        data1.user = obj
        data1.quantity = count

        data1.save()
        return redirect('customer_productview')
    return render(request, 'Customer/customer_buy.html')
@login_required(login_url='login_view')

def orders(request):
    user = request.user
    obj = Customer.objects.get(user=user)
    data = Buy.objects.filter(user=obj)
    return render(request, 'Customer/orders.html', {'data': data})
@login_required(login_url='login_view')
def add_to_cart(request,id):
    user = request.user
    obj = Customer.objects.get(user=user)
    data=Product.objects.get(id=id)
    print(data)
    print(obj)

    data1 = Cart()
    data1.product = data
    data1.user = obj
    data1.save()

    return redirect('cart_view')
    return render(request, 'Customer/customer_productview.html')

@login_required(login_url='login_view')


def cart_view(request):
    user = request.user
    obj = Customer.objects.get(user=user)
    data = Cart.objects.filter(user=obj)
    return render(request, 'Customer/cart_view.html', {'data': data})
@login_required(login_url='login_view')
def remove_product(request,id):
    data = Cart.objects.get(id=id)
    data.delete()
    return redirect('cart_view')
@login_required(login_url='login_view')

def cart_buy(request,id):
    user = request.user
    obj = Customer.objects.get(user=user)

    cart=Cart.objects.get(id=id)
    print(cart)

    data=cart.product
    print(data)

    count = request.POST.get("count")

    if request.method == 'POST':

        data1 = Buy()
        data1.product= data
        data1.user = obj
        data1.quantity = count
        data1.save()
        data = Cart.objects.get(id=id)
        data.delete()

        return redirect('customer_productview')
    return render(request, 'Customer/customer_buy.html')
@login_required(login_url='login_view')

def cancel_order(request,id):
    data = Buy.objects.get(id=id)
    data.delete()
    return redirect('orders')





















