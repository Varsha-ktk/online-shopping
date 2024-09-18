from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from e_app.forms import SellerForm, CustomerForm, LoginForm, ProductForm
from e_app.models import Customer, Seller, Product


# Create your views here.
def home(request):
    return render(request,'home.html')
def Login(request):
    return render(request,'login.html')
def pluto(request):
    return render(request,'pluto1.html')
def corona(request):
    return render(request,'corona.html')

def adminbase(request):
    return render(request, 'Admin/admin_base.html')



def customerbase(request):
    return render(request,'Customer/customer_base.html')
def sellerbase(request):
    return render(request,'Seller/seller_base.html')

def customer(request):
    data1=LoginForm()
    data2=CustomerForm()
    if request.method == 'POST':
        user1=LoginForm(request.POST)
        user2 = CustomerForm(request.POST,request.FILES)
        if user1.is_valid() and  user2.is_valid():
            form1=user1.save(commit=False)
            form1.is_customer=True
            form1.save()

            form2 = user2.save(commit=False)
            form2.user=form1
            form2.save()
            return redirect('login_view')

    return render(request,'regster_base.html',{'form1':data1,'form2':data2})

def seller(request):

    data1 = LoginForm()
    data2 = SellerForm()
    if request.method == 'POST':
        user1 = LoginForm(request.POST)
        user2 = SellerForm(request.POST,request.FILES)
        if user1.is_valid() and user2.is_valid():
            form1 = user1.save(commit=False)
            form1.is_seller = True
            form1.save()

            form2 = user2.save(commit=False)
            form2.user = form1
            form2.save()
            return redirect('login_view')

    return render(request,'regster_base.html',{'form1':data1,'form2':data2})

def login_view(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminbase')
            if user.is_seller:
                return redirect('sellerbase')
            if user.is_customer:
                return redirect('customerbase')
        else:
            messages.info(request,'invalid credential')
    return render(request,'login.html')






