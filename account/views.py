#-*- encoding: utf-8 -*-
from django.shortcuts import render, HttpResponseRedirect, HttpResponse, reverse, render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, UserRegistrationForm, CustomerRegistrationForm, UserEditForm, ProfileEditForm
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from rental.models import Reservation
from django.contrib.auth.models import User
from .models import Customer
from django.core.mail import send_mail
from django.contrib import messages

def indexView(request):
    return render(request, 'account/index.html')

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
            else:
                messages.error(request, '로그인에 실패했습니다. 계정 또는 비밀번호가 올바르지 않습니다')
                return redirect('account:login')

@login_required(login_url='/accounts/login/')
def logoutView(request):
    logout(request)
    return redirect(reverse('account:login'))

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        customer_form = CustomerRegistrationForm(request.POST, request.FILES)

        if user_form.is_valid() and customer_form.is_valid():
            #유저 생성
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            #생성한 유저를 고객에 연결
            Customer.objects.create(user=new_user, image=customer_form.cleaned_data['image'])
            #메인페이지로 리다이렉트
            return redirect('/')
        else:
            messages.error(request, '정보가 올바르지 않습니다. 다시 입력해주세요')
            return redirect(reverse('account:register'))

    else:
        user_form = UserRegistrationForm()
        customer_form = CustomerRegistrationForm()

        return render(request, 'account/register.html',  {'user_form': user_form,
        'customer_form': customer_form})

#마이페이지
#현재는 주문한내용만 보여줌
@login_required(login_url='/accounts/login/')
def mypage(request):
    user = User.objects.get(username=request.user)
    customer = Customer.objects.get(user=user)
    reservation = Reservation.objects.filter(customer=customer)

    return render(request, 'account/mypage.html', {'items': reservation})

@login_required(login_url='/accounts/login/')
def profile(request):
    user = User.objects.get(username=request.user)
    customer = Customer.objects.get(user=user)

    # 폼을 리턴
    if request.method == "GET":
        userform = UserEditForm(instance=user)
        profileform = ProfileEditForm(instance=customer)

        return render(request, 'account/profile.html', {'userform': userform, 'profileform': profileform})

    elif request.method == "POST":
        userform = UserEditForm(instance=user, data=request.POST)
        profileform = ProfileEditForm(instance=customer, data=request.POST, files=request.FILES)

        if userform.is_valid() and profileform.is_valid():
            userform.save()
            profileform.save()

        userform = UserEditForm(instance=user)
        profileform = ProfileEditForm(instance=customer)

        return render(request, 'account/profile.html', {'userform': userform, 'profileform': profileform})
