# -*- coding: utf-8 -*-

from django.shortcuts import render, redirect, get_object_or_404
from .forms import SigunguForm
from django.views.generic import FormView
from address.models import Sido, Sigungu, Address
from shop.models import Store
from rental.models import Rentalinventory, RentalProduct
from django.core.exceptions import ObjectDoesNotExist

#렌탈 검색
class searchRentalProduct(FormView):
    template_name = 'rental/search.html'
    form_class = SigunguForm

    def get(self, request, *args, **kwargs):
        form = self.get_form(self.form_class)
        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        sido_name = form.cleaned_data['sido']
        sigungu_name = form.cleaned_data['sigungu']

        try:
            #예외처리 필요함
            #도중에 아무것도 없을 경우 None을 리턴해야 할듯
            sigungu = Sigungu.objects.get(sido=sido_name, name=sigungu_name)
            address = Address.objects.get(Sigungu=sigungu)
            store = Store.objects.get(address=address)

            #인벤토리 검색
            inventory = Rentalinventory.objects.filter(store=store)

        except ObjectDoesNotExist:
            inventory = None

        return render(self.request, 'rental/list.html', {'inventory': inventory})

#상품을 자세히 보여준다.
#인벤토리 id는 꼭 필요하며,
def detail_RentalProduct(request, inventory_id):
    inventory = get_object_or_404(Rentalinventory, pk = inventory_id)
    return render(request, 'rental/detail.html', {'inventory':inventory})


#예약
#로그인 필요
def make_reservation(requet):
    pass
