# -*- coding: utf-8 -*-
from account.models import Customer
from address.models import Address, Sigungu
from rental.models import RentalCategory, RentalProduct, Rentalinventory
from shop.models import Store
import random
import string

#핸드폰 번호 랜덤 생성
def RandGenerator_phone():
    first = str(random.randint(100,999))
    second = str(random.randint(1,888)).zfill(3)

    last = (str(random.randint(1,9998)).zfill(4))
    while last in ['1111','2222','3333','4444','5555','6666','7777','8888']:
        last = (str(random.randint(1,9998)).zfill(4))

    return '{}-{}-{}'.format(first,second, last)

#난수 숫자 생성기
def RandGenerator(max):
    return random.randrange(1, max) + 1

#난수 문자생성기
def RandGenerator_String():
	s = string.lowercase + string.digits
	return ''.join(random.sample(s,10))

#고객의 갯수를 구한다.
def getCountOfCustomer():
    return Customer.objects.count()

#존재하는 고객을 랜덤으로 선택해서 리턴한다.
def getRandCustomer():
    countOfCustomer = getCountOfCustomer()
    customer_id = RandGenerator(countOfCustomer)

    return Customer.objects.get(id=customer_id)

################################# 주소 ######################################

#주소의 갯수를 구한다.
def getCountOfAddress():
    return Address.objects.count()

#존재하는 주소를 랜덤으로 선택해서 리턴한다.
def getRandAddress():
    countOfAddress = getCountOfAddress()
    address_id = RandGenerator(countOfAddress)

    return Address.objects.get(id=address_id)

def getCountOfSigungu():
    return Sigungu.objects.count()

def getRandSigungu():
    countOfSigungu = getCountOfSigungu()
    sigungu_id = RandGenerator(countOfSigungu)

    return Sigungu.objects.get(id=sigungu_id)

################################# 상품 ######################################

def getCountOfRentalCategory():
    return RentalCategory.objects.count()

def getRandRentalCategory():
    countOfCateogyr = getCountOfCustomer()
    Category_id = RandGenerator(countOfCateogyr)

    return RentalCategory.objects.get(id=Category_id)

def getCountOfRentalProduct():
    return RentalProduct.objects.count()

def getRandRentalProduct():
    countOfProudct = getCountOfRentalProduct()
    product_id = RandGenerator(countOfProudct)

    return RentalProduct.objects.get(id=product_id)

def getCountOfRentalinventory():
    return Rentalinventory.objects.count()

def getRandRentalinventory():
    countinventory = getCountOfRentalinventory()
    inventory_id = RandGenerator(countinventory)

    return Rentalinventory.objects.get(id=inventory_id)

################################# 상점 ######################################

def getCountOfStore():
    return Store.objects.count()

def getRandStore():
    countOfStore = getCountOfStore()
    store_id = RandGenerator(countOfStore)

    return Store.objects.get(id=store_id)