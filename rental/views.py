# -*- coding: utf-8 -*-

from django.shortcuts import render
from .forms import SigunguForm
from django.views.generic import FormView
from address.models import Sido, Sigungu, Address
from shop.models import Store
from rental.models import Rentalinventory, RentalProduct

#렌탈 검색 폼
class searchRentalProduct(FormView):
    template_name = 'rental/search.html'
    form_class = SigunguForm

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        sido_name = form.cleaned_data['sido']
        sigungu_name = form.cleaned_data['sigungu']

        #예외처리 필요함
        #도중에 아무것도 없을 경우 None을 리턴해야 할듯
        sigungu = Sigungu.objects.get(sido=sido_name, name=sigungu_name)
        address = Address.objects.get(Sigungu=sigungu)
        store = Store.objects.get(address=address)

        #인벤토리 검색
        inventory = Rentalinventory.objects.filter(store=store)
        print inventory, '\n', '\n'
        return render(self.request, 'rental/detail.html', {'inventory':inventory})











