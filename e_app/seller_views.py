from django.shortcuts import render, redirect

from e_app.forms import ProductForm
from e_app.models import Seller, Product


def product(request):
    seller = request.user   #  to get user id
    print(seller)
    obj = Seller.objects.get(user = seller)# to get seller id
    print(obj.id)
    data=ProductForm()

    if request.method == 'POST':
        user2 = ProductForm(request.POST,request.FILES)
        if user2.is_valid():
            form1 = user2.save(commit=False)
            form1.user = obj
            form1.save()
            return redirect('product_view')
    return render(request,'Seller/product.html',{'data1':data})

def product_view(request):
    user=request.user #user id
    obj = Seller.objects.get(user=user) #obj id in seller table
    data1 = Product.objects.filter(user=obj)
    print(obj.id)
    print(user.id)
    print(data1)
    return render(request,'Seller/product_view.html',{'data1':data1})

def product_delete(request,id):
    data=Product.objects.get(id=id)
    data.delete()
    return redirect('product_view')

def product_update(request,id):
    data=Product.objects.get(id=id)
    form=ProductForm(instance=data)
    if request.method=='POST':
        updated_data=ProductForm(request.POST,request.FILES,instance = data)
        updated_data.is_valid()
        updated_data.save()
        return redirect('product_view')

    return render(request,'seller/product_update.html',{'form':form})

