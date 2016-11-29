# -*- encoding: utf-8 -*-
from django import forms

QUANTITY_CHOCIES = [(i, str(i)) for i in range(1, 12)]

class AddCartForm(forms.Form):
    #quantity = forms.TypedChoiceField(choices=QUANTITY_CHOCIES, coerce=int, label='수량')
    #quantity = forms.TypedChoiceField(label='수량')
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control'}))
