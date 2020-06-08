from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def Home_Page(request):
    return render(request,'accounts/home.html')
def Customer(request):
    return render(request,'accounts/customer.html')


@login_required
def Customer(request):
    return render(request,'MyApp/Customer.html')

