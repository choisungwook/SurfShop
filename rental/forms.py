# -*- coding: utf-8 -*-
from django import forms

from address.models import Address, Sido, Sigungu
from django.forms import ModelChoiceField
from shop.models import Store
from address.models import Sigungu, Sido, Address
from rental.models import Rentalinventory

def queryset():
    rental = Rentalinventory.objects.all().values_list('store')
    store = Store.objects.filter(id__in=rental).values_list('address')
    address = Address.objects.filter(id__in=store).values_list('Sigungu')
    sigungu = Sigungu.objects.filter(id__in=address).values_list('sido')

    return Sido.objects.filter(id__in=sigungu)

class SigunguForm(forms.Form):
    sido = forms.ModelChoiceField(label="시도", widget=forms.Select(attrs={'class' : 'form-control'}),
    queryset= queryset())
    sigungu = forms.CharField(label="시군구", widget=forms.Select(attrs={'class' : 'form-control'}))
