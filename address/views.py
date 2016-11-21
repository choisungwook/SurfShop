# -*- coding: utf-8 -*-
from .models import Sido, Sigungu
from django.http import JsonResponse
import json


#JSON
#시도로 시군구를 검색한다.
def searchSigungu(request):
    # 시도 id를 찾는다.
    sido = request.GET.get('sido_id')

    # 찾은 id를 가지고 있는 시군구를 가져와서
    # json으로 직렬화 한다음 리턴한다
    sigungus = Sigungu.objects.filter(sido=sido)
    json_res = []

    for row in sigungus:
        json_obj = dict(name=row.name)
        json_res.append(json_obj)

    return JsonResponse(json.dumps(json_res), safe=False)