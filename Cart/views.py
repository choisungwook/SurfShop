# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from .cart import Cart
from rental.models import Rentalinventory
from django.views.generic import FormView
from .forms import AddCartForm
from django.views.decorators.http import require_POST

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
            HttpResponse('[Error] 주문수량이 기존수량보다 많습니다')

    return redirect('cart:detail')

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
