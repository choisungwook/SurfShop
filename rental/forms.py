# -*- coding: utf-8 -*-
from django import forms

from address.models import Address, Sido, Sigungu
from django.forms import ModelChoiceField
from shop.models import Store
from address.models import Sigungu, Sido, Address

class SigunguForm(forms.Form):
    sido = forms.ModelChoiceField(label="시도", widget=forms.Select(attrs={'class' : 'form-control'}), queryset=Sido.objects.filter(id__in=Sigungu.objects.filter(id__in= \
                                                    Address.objects.filter(id__in=Store.objects.values_list('address').distinct()).values_list('Sigungu').distinct()).values_list('sido_id')))
    sigungu = forms.CharField(label="시군구", widget=forms.Select(attrs={'class' : 'form-control'}))
