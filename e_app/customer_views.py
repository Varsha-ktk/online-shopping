from django.shortcuts import render

from e_app.models import Customer, Product


def customer_productview(request):
    data=Product.objects.all()
    return render(request,'Customer/customer_productview.html',{'data':data})
