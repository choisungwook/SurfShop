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
from django.core.files.uploadedfile import SimpleUploadedFile
#현재 디렉토리
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
NAME_FILE = os.path.join(os.path.dirname(__file__), 'name.lst')
#고객 사진(강아지)
CUSTOMER_DIR = os.path.join(BASE_DIR, 'customer')
#카테고리 : 옷
CLOTHES_DIR = os.path.join(BASE_DIR, 'Clothes')
#카테고리 : 보드
BOARD_DIR = os.path.join(BASE_DIR, 'Surfboard')
#카테고리 : 악세사리
ACCESSORY_DIR = os.path.join(BASE_DIR, 'Accessory')
#카테고리
category_name = ['Accessory', 'Clothes', 'Surfboard']

#카테고리 : 보드
#고객 생성
#장고에서 지원하는 유저 모델을 외래키로 1:1 연결(상속 개념)해서 새로운 유저 모델을 만든다
#이 원리를 사용하면 여러개의 유저를 확장할 수 있고
#다른 방법으로는 장고에서 지원하는 권한, 그룹 기능으로 관리할 수 있다.
def test_model_create_Customer():
    #유저 생성
    user = test_model_create_User()
    #주소 생성
    address = test_models_create_Address()
    images = os.listdir(CUSTOMER_DIR)
    image = random.choice(images)
    #장고형식으로 이미지 변경
    img = open(os.path.join(CUSTOMER_DIR, image), 'rb')
    uploaded = SimpleUploadedFile(img.name, img.read())
    return Customer.objects.create(image=uploaded, user=user, address=address)

#유저 생성
def test_model_create_User():
    username = utility.RandGenerator_String() + "@aaa.com"
    password = 'abcdef'

    return User.objects.create_user(username=username, password=password)

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
    #이름 가져오기
    names = []
    Fnames = open(NAME_FILE, 'r')
    for name in Fnames:
        names.append(name)

    name = random.choice(names)
    # name = utility.RandGenerator_String()
    return Store.objects.create(address=address, name=name)

#렌탈 카테고리 생성
def test_models_create_RentalCategory():
    #이름 랜덤 생성
    for name in category_name:
        slug = slugify(name)
        RentalCategory.objects.create(name=name, slug=slug)

#장고형식으로 이미지타입 변경
def create_djangoImageType(Dir, image):
    #장고형식으로 이미지 변경
    img = open(os.path.join(Dir, image), 'rb')
    uploaded = SimpleUploadedFile(img.name, img.read())

    return uploaded

#상품 만든다.
def test_models_create_Product(image, name, category):
    description = utility.RandGenerator_String()
    price = utility.RandGenerator(10000)
    last_update = timezone.now()
    published = timezone.now()
    available = True
    stock = utility.RandGenerator(100)
    #slug 생성
    for x in itertools.count(1):
        if not RentalProduct.objects.filter(slug=x).exists():
            slug = slugify(x)
            break

    category = RentalCategory.objects.get(name=category)
    RentalProduct.objects.create(category=category, name=name, price=price, last_update=last_update, slug=slug,
                                 description=description, published=published, image=image, available=available, stock=stock)

def test_models_create_RentalProduct():
    category_name = ['Accessory', 'Clothes', 'Surfboard']

    for category in category_name:
        if category is 'Accessory':
            files = os.listdir(ACCESSORY_DIR)
            namecount = 1
            for file in files:
                image = create_djangoImageType(ACCESSORY_DIR, file)
                test_models_create_Product(image, 'Accessory' + str(namecount), 'Accessory')
                namecount+=1
        elif category is 'Surfboard':
            files = os.listdir(BOARD_DIR)
            namecount = 1
            for file in files:
                image = create_djangoImageType(BOARD_DIR, file)
                test_models_create_Product(image, 'Surfboard' + str(namecount), 'Surfboard')
                namecount+=1
        elif category is 'Clothes':
            files = os.listdir(CLOTHES_DIR)
            namecount = 1
            for file in files:
                image = create_djangoImageType(CLOTHES_DIR, file)
                test_models_create_Product(image, 'Clothes' + str(namecount), 'Clothes')
                namecount+=1

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
    stock = 0


    while true:
        stock = utility.RandGenerator(10)
        if stock <= inventory.rentalproduct.stock:
            break;

    Reservation.objects.create(customer=customer, inventory=inventory, in_date=in_date, out_date=out_date,
                               status=status, stock=stock)

    #재고를 빼줌
    inventory.rentalproduct.stock -= stock
    inventory.save()

def run():
    #고객 생성
    print '[INFO] start create Customer'
    try:
        for x in range(100):
            test_model_create_Customer()
    except:
        print '[ERROR] ERROR create Customer'
    print '[INFO] finish create Customer'

    #렌탈 카테고리 생성
    print '[INFO] start create category'
    try:
        test_models_create_RentalCategory()
    except:
        print '[Error] Error create category'
    print '[INFO] Finish create category'

    # # #렌탈 상품 생성
    print '[INFO] START create Rental Product'
    test_models_create_RentalProduct()
    print '[INFO] FINISH create Rental Product'

    # # 상점 생성
    print '[INFO] START create STORE'
    for x in range(100):
        test_models_create_Store()
    print '[INFO] FINISH create STORE'

    #렌탈 인벤토리 생성
    print '[INFO] START create INVENTORY'
    for x in range(100):
        test_models_create_RentalInventory()
    print '[INFO] FINISH create INVENTORY'

    #print '[INFO] START create RESERVATIOn'
    #for x in range(100):
    #    test_models_create_Reservation()
    #print '[INFO] FINISH create RESERVATIOn'

    print 'ALL TEST Finished'
