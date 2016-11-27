# -*- coding: utf-8 -*-
from django import forms

from address.models import Address, Sido, Sigungu
from django.forms import ModelChoiceField
from shop.models import Store
from address.models import Sigungu, Sido, Address

class SigunguForm(forms.Form):
    sido = forms.ModelChoiceField(widget=forms.Select, queryset=Sido.objects.filter(id__in=Sigungu.objects.filter(id__in= \
                                                    Address.objects.filter(id__in=Store.objects.values_list('address').distinct()).values_list('Sigungu').distinct()).values_list('sido_id')))
    sigungu = forms.CharField(widget=forms.Select)
