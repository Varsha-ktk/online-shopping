from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from e_app.forms import SellerForm
from e_app.models import Customer, Seller, Product


@login_required(login_url='login_view')
def admin_customerview(request):
    data1 = Customer.objects.all()
    print(data1)
    return render(request,'Admin/admin_customerview.html',{'data1':data1})

@login_required(login_url='login_view')
def admin_sellerview(request):
    data1 = Seller.objects.all()
    print(data1)
    return render(request,'Admin/admin_sellerview.html',{'data1':data1})

@login_required(login_url='login_view')
def seller_delete(request,id):
    data=Seller.objects.get(id=id)
    data.delete()
    return redirect('admin_sellerview')

@login_required(login_url='login_view')
def customer_delete(request,id):
    customer_data=Customer.objects.get(id=id)
    customer_data.delete()
    return redirect('admin_customerview')

@login_required(login_url='login_view')
def seller_update(request,id):
    data=Seller.objects.get(id=id)
    form=SellerForm(instance=data)
    if request.method=='POST':
        updated_data=SellerForm(request.POST,request.FILES,instance = data)
        updated_data.is_valid()
        updated_data.save()
        return redirect('admin_sellerview')

    return render(request,'Admin/admin_sellerupdate.html',{'form':form})

@login_required(login_url='login_view')
def admin_productview(request):
    data=data=Product.objects.all()
    return render(request, 'Admin/admin_productview.html', {'data': data})

