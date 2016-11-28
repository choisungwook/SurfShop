# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect, reverse, HttpResponse
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

def list_storeRentalProduct(request):
    form = SigunguForm(request.GET)
    cart_product_form = AddCartForm()

    if form.is_valid():
        sido_name = form.cleaned_data['sido']
        sigungu_name = form.cleaned_data['sigungu']

        #예외처리
        #도중에 아무것도 없을 경우 None을 리턴
        try:
            sigungu = Sigungu.objects.filter(sido=sido_name, name=sigungu_name)
            address = Address.objects.filter(Sigungu=sigungu)
            store = Store.objects.filter(address__in=address)

            #인벤토리 검색
            inventory = Rentalinventory.objects.filter(store__in=store)
        except ObjectDoesNotExist:
            inventory = None

        return render(request, 'rental/list.html', {'inventory': inventory,
        'cart_product_form':cart_product_form})


#상품을 자세히 보여준다.
#인벤토리 id는 꼭 필요하며,
def detail_RentalProduct(request, inventory_id):
    cart_product_form = AddCartForm()
    form = SigunguForm()
    inventory = get_object_or_404(Rentalinventory, pk = inventory_id)

    return render(request, 'rental/detail.html', {'inventory':inventory,
    'cart_product_form':cart_product_form})

#예약
#로그인 필요
@login_required(login_url='account:login')
def make_reservation(request):
    cart = Cart(request)
    user = User.objects.get(username=request.user)
    customer = Customer.objects.get(user=user)

    #예약하기 위해서는 수량을 체크해야됨
    #주문할려는 상품의 갯수가 현재 잔고보다 많은 경우 주문이 안되고 에러메세지를 출력해야됨
    for inventory in cart:
        if inventory['inventory'].rentalproduct.stock < inventory['quantity']:
            return HttpResponse('[Error] 예약수량이 기존상품보다 많습니다')

    for inventory in cart:
        stock = inventory['inventory'].rentalproduct.stock - inventory['quantity']
        inventory['inventory'].rentalproduct.stock = stock
        inventory['inventory'].rentalproduct.save()

        Reservation.objects.create(customer=customer, inventory=inventory['inventory'], in_date=timezone.now(),
        out_date=timezone.now(), status=0, stock=inventory['quantity'])

        #주문이 완료되면 장바구니에서 삭제한다.
        cart.remove(inventory['inventory'])

    return HttpResponseRedirect(reverse('account:mypage'))
