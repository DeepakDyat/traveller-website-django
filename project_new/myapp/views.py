from django.conf import settings
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.db import transaction
from django.shortcuts import render, redirect

# Create your views here.
from .forms import CreateUserForm, contactForm, bookingForm

from django.contrib.auth.models import User

from .models import package, checkout


def index(request):
    return render(request,'index.html')

def hello(request):
    return render(request,'second.html')

def register(request):
    form=CreateUserForm()
    if request.user.is_authenticated:
        messages.info(request,"already registered")
        return redirect('index')

    else:
        if request.method=="POST":
            form=CreateUserForm(request.POST)
            if form.is_valid():
                email=form.cleaned_data.get('email')
                form.save()
                send_mail(
                    'Confirmation mail',
                    'Thanks for register here!',
                    settings.EMAIL_HOST_USER,
                    fail_silently=True,
                    recipient_list=[email]


                )
                user=form.cleaned_data.get('username')
                messages.success(request,"registered successfully!"+user)
            else:
                messages.error(request,"fill correct details")
                return redirect('register')
            return redirect('login')
    return render(request,'register.html',{'form':form})


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            user=authenticate(request,username=username,password=password)

            if user is not None:
                login(request,user)
                messages.success(request,"login successully")
                return redirect('index')
            else:
                messages.error(request,"Username Or Paasword is incorrect")
    return render(request,'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')



def enquiry(request):
    form=contactForm()
    if request.method=="POST":
        form=contactForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data.get('email')
            form.save()
            send_mail(
                    'Confirmation mail',
                    'Thanks for Contact us!! Stay connected for more information and queries...',
                    settings.EMAIL_HOST_USER,
                    fail_silently=True,
                    recipient_list=[email]


                )
            messages.success(request,"data submitted!!")
        else:
            messages.error(request,"fill the correct details")



    return render(request,'enquiry.html',{'form':form})

def packs(request):
    p1=package.objects.all()
    return render(request,'packs.html',{'p1':p1})


def order(request):
    form = bookingForm()
    if request.method == "POST":
        form = bookingForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            form.save()
            send_mail(
                'Confirmation mail',
                'Thanks for booking.. stay connectd with us for booking various packages',
                settings.EMAIL_HOST_USER,
                fail_silently=True,
                recipient_list=[email]

            )
            messages.success(request, "package booked successfully !!")
        else:
            messages.error(request, "fill the correct details")
    else:


        idd = request.GET["checkid"]
        obj = package.objects.get(id=idd)

    return render(request,'order.html',{'form':form,'obj':obj})


def payment(request):
    if request.method == "POST":
        name = request.POST.get('name')
        card_no = request.POST.get('card_no')
        expiry = request.POST.get('expiry')
        cvv = request.POST.get('cvv')
        demo = checkout(name=name,card_no=card_no,expiry=expiry,cvv=cvv)
        demo.save()
        messages.success(request, 'Your payment is successful\n Thanks for booking ')
        return redirect('index')

    return render(request,'payment.html')