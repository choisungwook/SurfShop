# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from address.models import Address
import random, string

def RandString():
	s = string.lowercase + string.digits
	return ''.join(random.sample(s,10))

####핸드폰 번호 자동 생성
def gen_phone():
    first = str(random.randint(100,999))
    second = str(random.randint(1,888)).zfill(3)

    last = (str(random.randint(1,9998)).zfill(4))
    while last in ['1111','2222','3333','4444','5555','6666','7777','8888']:
        last = (str(random.randint(1,9998)).zfill(4))

    return '{}-{}-{}'.format(first,second, last)

def CreateCustomer():
    pass

def CreateUser():
    username = RandString()
    email = username + "@aaa.com"
    password = 'abcdef'

    User.objects.create_user(username=username, email=email, password=password)

def test_models_Create_Address():
    #시군구 랜덤함수로 뽐음 (1~250)
    sigungu = random.randrange(1,250) + 1
    phone = gen_phone()
    other_address = '미정'

    Address.objects.create(Sigungu=sigungu, other_address=other_address, phone=phone)

def run():
    test_models_Create_Address()




