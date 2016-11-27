# -*- coding: utf-8 -*-
from .models import Sido, Sigungu, Address
from django.http import JsonResponse
from shop.models import Store
import json

#JSON
#시도로 시군구를 검색한다.
def searchSigungu(request):
    # 시도 id를 찾는다.
    sido = request.GET.get('sido_id')

    #중복된 상점 주소 제거
    distinct_store = Store.objects.values_list('address').distinct()
    distinct_address =  Address.objects.filter(id__in=distinct_store).values_list('Sigungu').distinct()
    #해당 시에서 존재하는 시,군,구만 검색
    distinct_sigungu = Sigungu.objects.filter(id__in=distinct_address, sido_id=sido)

    # sigungus = Sigungu.objects.filter(sido=sido)
    json_res = []

    # 찾은 id를 가지고 있는 시군구를 가져와서
    # json으로 직렬화 한다음 리턴한다
    for row in distinct_sigungu:
        json_obj = dict(name=row.name)
        json_res.append(json_obj)

    return JsonResponse(json.dumps(json_res), safe=False)
