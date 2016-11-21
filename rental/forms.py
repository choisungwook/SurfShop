from django import forms

from address.models import Address, Sido, Sigungu
from django.forms import ModelChoiceField

class SigunguForm(forms.Form):
    sido = forms.ModelChoiceField(widget=forms.Select, queryset=Sido.objects.all())
    sigungu = forms.CharField(widget=forms.Select)

    def __init__(self, *args, **kwargs):
        super(SigunguForm, self).__init__(*args, **kwargs)