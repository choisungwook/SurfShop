# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse
from .forms import SigunguForm
from django.views.generic import FormView
from address.models import Sido, Sigungu, Address
from shop.models import Store
from rental.models import Rentalinventory, RentalProduct, Reservation
from django.core.exceptions import ObjectDoesNotExist
from Cart.forms import AddCartForm
from Cart.cart import Cart
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from account.models import Customer
from django.core.exceptions import ObjectDoesNotExist

#렌탈 검색
def searchRentalProduct(request):
    if request.method == "GET":
        form = SigunguForm()
        return render(request, 'rental/search.html', {'form': form})

    elif request.method == "POST":
        form = SigunguForm(request.POST)
        cart_product_form =  AddCartForm()

        if form.is_valid():
            sido_name = form.cleaned_data['sido']
            sigungu_name = form.cleaned_data['sigungu']

            try:
                #예외처리 필요함
                #도중에 아무것도 없을 경우 None을 리턴해야 할듯
                sigungu = Sigungu.objects.get(sido=sido_name, name=sigungu_name)
                address = Address.objects.get(Sigungu=sigungu)
                store = Store.objects.get(address=address)

                #인벤토리 검색
                inventory = Rentalinventory.objects.filter(store=store)

            except ObjectDoesNotExist:
                inventory = None

            return render(request, 'rental/list.html', {'inventory': inventory,
            'cart_product_form':cart_product_form})

#상품을 자세히 보여준다.
#인벤토리 id는 꼭 필요하며,
def detail_RentalProduct(request, inventory_id):
    inventory = get_object_or_404(Rentalinventory, pk = inventory_id)
    return render(request, 'rental/detail.html', {'inventory':inventory})

#예약
#로그인 필요
@login_required(login_url='account:login')
def make_reservation(request):
    cart = Cart(request)
    user = User.objects.get(username=request.user)
    customer = Customer.objects.get(user=user)

    for inventory in cart:
        reservation = Reservation.objects.filter(customer=customer, inventory=inventory['inventory'])

        if reservation.exists():
            reservation.update(stock=inventory['quantity'])
        else:
            Reservation.objects.create(customer=customer, inventory=inventory['inventory'], in_date=timezone.now(),
            out_date=timezone.now(), status=0, stock=inventory['quantity'])

    return HttpResponseRedirect(reverse('account:mypage'))
