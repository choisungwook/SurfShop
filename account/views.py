#-*- encoding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse, render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from rental.models import Reservation
from django.contrib.auth.models import User
from .models import Customer
from django.core.mail import send_mail

#로그인
def loginView(request):
    if request.method == "GET":
        form = LoginForm()
        return render(request, 'account/login.html', {'form': form})

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('rental:rentalsearch'))
                    #return HttpResponse('Authenticated successfully')

                else:
                    return HttpResponse('Disabled account')

@login_required(login_url='/accounts/login/')
def logoutView(request):
    logout(request)
    return redirect(reverse('account:login'))

#마이페이지
#현재는 주문한내용만 보여줌
@login_required(login_url='/accounts/login/')
def mypage(request):
    user = User.objects.get(username=request.user)
    customer = Customer.objects.get(user=user)
    reservation = Reservation.objects.filter(customer=customer)

    return render(request, 'account/mypage.html', {'items': reservation})
