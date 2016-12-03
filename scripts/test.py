# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from address.models import Address, Sigungu
from account.models import Customer
from shop.models import Store
from rental.models import RentalCategory, RentalProduct, Rentalinventory, Reservation
from django.utils import timezone
from django.utils.text import slugify
import utility
import itertools
import random
import os
NAME_FILE = os.path.join(os.path.dirname(__file__), 'name.lst')

#고객 생성
#장고에서 지원하는 유저 모델을 외래키로 1:1 연결(상속 개념)해서 새로운 유저 모델을 만든다
#이 원리를 사용하면 여러개의 유저를 확장할 수 있고
#다른 방법으로는 장고에서 지원하는 권한, 그룹 기능으로 관리할 수 있다.
def test_model_create_Customer():
    #유저 생성
    user = test_model_create_User()
    #주소 생성
    address = test_models_create_Address()

    return Customer.objects.create(image=None, user=user, address=address)

#유저 생성
def test_model_create_User():
    names = []
    #이름 가져오기
    Fnames = open(NAME_FILE, 'r')
    for name in Fnames:
        names.append(name)

    username = random.choice(names)
    email = utility.RandGenerator_String() + "@aaa.com"
    password = 'abcdef'

    return User.objects.create_user(username=username, email=email, password=password)

#주소 생성
def test_models_create_Address():
    #시군구 함수를 선택함
    sigungu = utility.getRandSigungu()
    #주소를 가져오고 나머지 지정
    phone = utility.RandGenerator_phone()
    other_address = utility.RandGenerator_String()

    return Address.objects.create(Sigungu=sigungu, other_address=other_address, phone=phone)

#상점 생성성
def test_models_create_Store():
    #주소 생성
    address = test_models_create_Address()
    #이름 랜덤 생성
    name = utility.RandGenerator_String()

    return Store.objects.create(address=address, name=name)

#렌탈 카테고리 생성
def test_models_create_RentalCategory():
    #이름 랜덤 생성
    name = utility.RandGenerator_String()
    slug = slugify(name)

    return RentalCategory.objects.create(name=name, slug=slug)

def test_models_create_RentalProduct():
    category = utility.getRandRentalCategory()
    name = utility.RandGenerator_String()
    description = utility.RandGenerator_String()
    price = utility.RandGenerator(10000)
    last_update = timezone.now()
    published = timezone.now()
    image = None
    available = True
    stock = utility.RandGenerator(100)

    #slug 생성
    for x in itertools.count(1):
        if not RentalProduct.objects.filter(slug=x).exists():
            slug = '%d' % x
            break

    return RentalProduct.objects.create(category=category, name=name, price=price, last_update=last_update, slug=slug,
                                 description=description, published=published, image=image, available=available, stock=stock)

#렌탈 인벤토리 생성
def test_models_create_RentalInventory():
    rentalproduct = utility.getRandRentalProduct()
    store = utility.getRandStore()

    return Rentalinventory.objects.create(rentalproduct=rentalproduct, store=store)

#Rental 생성
def test_models_create_Reservation():
    customer = utility.getRandCustomer()
    inventory = utility.getRandRentalinventory()
    in_date = timezone.now()
    out_date = timezone.now()
    status = 0
    stock = utility.RandGenerator(10)

    print customer, inventory, status, stock

    Reservation.objects.create(customer=customer, inventory=inventory, in_date=in_date, out_date=out_date,
                               status=status, stock=stock)

def run():
    # #고객 생성
    print '[INFO] start create Customer'
    try:
        for x in range(100):
            test_model_create_Customer()
    except:
        pass
    print '[INFO] finish create Customer'
    #
    # # 상점 생성
    # print 'create Store'
    # for x in range(100):
    #     test_models_create_Store()
    #
    #렌탈 카테고리 생성
    # print 'create Rental cateory'
    # for x in range(100):
    #     test_models_create_RentalCategory()

    # #렌탈 상품 생성
    # print 'create Rental Product'
    # for x in range(100):
    #     test_models_create_RentalProduct()

    #렌탈 인벤토리 생성
    # print 'create inventory '
    # for x in range(100):
    #     test_models_create_RentalInventory()

    # print '예약 생성'
    # for x in range(100):
    #     test_models_create_Reservation()
