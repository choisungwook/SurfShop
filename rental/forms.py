from django import forms

from address.models import Address, Sido, Sigungu
from django.forms import ModelChoiceField
from shop.models import Store
from address.models import Sigungu, Sido, Address

class SigunguForm(forms.Form):
    #sido = forms.ModelChoiceField(widget=forms.Select, queryset=Sido.objects.all())
    # stores = Store.objects.all(address__Sigungu)
    # for store in stores:
    #     print store.address

    # addresss = Address.objects.all().filter(id__in=Sigungu.objects.all()).distinct()
    # print addresss
    # for address in addresss:
    #     print address
    sido = forms.ModelChoiceField(widget=forms.Select, queryset=Sido.objects.filter(id__in=Sigungu.objects.filter(id__in=Store.objects.all().values_list('address', flat=True).distinct())))
    sigungu = forms.CharField(widget=forms.Select)

    def __init__(self, *args, **kwargs):
        super(SigunguForm, self).__init__(*args, **kwargs)
