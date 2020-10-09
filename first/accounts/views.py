from django.shortcuts import render
from django.http import HttpResponse

from .models import *

def home(request):
    orders = order.objects.all()
    customers = customer.objects.all()

    total_customers=customers.count()
    total_orders=orders.count()

    delivered=orders.filter(status='delivered').count()
    pending=orders.filter(status='pending').count()

    context = {'orders':orders, 'customers':customers, 'total_customers':total_customers, 'total_orders':total_orders, 'delivered':delivered, 'pending':pending}

    return render(request,'accounts/dashboard.html',context)

def products(request):
    products = product.objects.all()
    return render(request,'accounts/products.html',{'products':products})  

def customers(request, pk_test):
    customers = customer.objects.get(id=pk_test)

    orders = customers.order_set.all()
    order_count = orders.count()


    context = {'customers':customers, 'orders':orders, 'order_count':order_count}
    return render(request,'accounts/customers.html',context)     
  

# Create your views here.
