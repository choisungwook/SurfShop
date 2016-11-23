# -*- coding: utf-8 -*-

from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from rental.models import Rentalinventory
#카트 추가
def add_to_cart(request, inventory_id):
    cart = Cart(request)
    inventory = get_object_or_404(Rentalinventory, id=inventory_id)
    cart.add(inventory=inventory, quantity=1, update_quantity=True)

    return redirect('cart:detail')

def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart':cart})

def remove_cartItem(request, inventory_id):
    cart = Cart(request)
    inventory = get_object_or_404(Rentalinventory, id=inventory_id)
    cart.remove(inventory)

    return redirect('cart:detail')
