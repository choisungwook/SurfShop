# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse, reverse
from .cart import Cart
from rental.models import Rentalinventory
from django.views.generic import FormView
from .forms import AddCartForm
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.http import Http404
from django.template import RequestContext

#카트추가
@require_POST
def add_to_cart(request, inventory_id):
    cart = Cart(request)
    form = AddCartForm(request.POST)
    inventory = get_object_or_404(Rentalinventory, id=inventory_id)

    if form.is_valid():
        cd = form.cleaned_data
        quantity = cd['quantity']

        #수량체크
        if inventory.rentalproduct.get_stock() >= quantity:
            cart.add(inventory=inventory, quantity=quantity)

        else:
            messages.error(request, '[Error] 주문수량이 기존수량보다 많습니다')
            refer = request.META['HTTP_REFERER']
            host = request.META['HTTP_HOST']
            url = refer.split(host)
            #수량이 일치하지 않으면 되돌아간다.
            #HTTP_HOST의 특성이 서버의 주소가 맞는지?..
            return redirect(url[1], {'messages':messages})

        return redirect('cart:detail')

def update_cart(request):
    pass

#카트 리스트(자세히)보기
def cart_detail(request):
    cart = Cart(request)

    for item in cart:
        item['update_quantity_form'] = AddCartForm(
        initial={'quantity': item['quantity']})

    return render(request, 'cart/detail.html', {'cart':cart})

def remove_cartItem(request, inventory_id):
    cart = Cart(request)
    inventory = get_object_or_404(Rentalinventory, id=inventory_id)
    cart.remove(inventory)

    return redirect('cart:detail')
