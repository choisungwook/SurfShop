# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse
from shop.models import Store
from account.models import Customer
from sorl.thumbnail import ImageField

#렌탈 상품 카테고리
class RentalCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        db_table = 'RentalCategory'
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __unicode__(self):
        return self.name

    def get_absoulte_url(self):
        return reverse('shop:product_list_by_category', args=[self.slug])

#렌탈 상품 모델
class RentalProduct(models.Model):
    category = models.ForeignKey(RentalCategory, related_name='products')
    name = models.CharField(max_length=45)
    description = models.TextField(blank=True)
    available = models.BooleanField(default=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    published = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    last_update = models.DateTimeField(blank=True, null=True, auto_now=True)
    image = models.ImageField(upload_to='%Y/%m/%d', blank=True)
    available = models.BooleanField(default=True)
    stock = models.PositiveIntegerField()
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        db_table = 'RentalProduct'
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __unicode__(self):
        return self.name

    def get_absoulte_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])

    def get_stock(self):
        return self.stock

    def iter_stock(self):
        dict_stock = []
        for x in range(1, self.stock + 1):
            dict_stock.append(x)
        return dict_stock

#렌탈 인벤토리 모델
#상점, 상품이랑 연결되어 있음
#검색때 유용하게 사용됨
class Rentalinventory(models.Model):
    store = models.ForeignKey(Store, related_name='store')
    rentalproduct = models.ForeignKey(RentalProduct, related_name='rentalproduct')

    class Meta:
        db_table = 'Rentalinventory'

    def __unicode__(self):
        return self.rentalproduct.name

#예약 모델
#상태코드 0 : 예약중, 1. 예약확인
class Reservation(models.Model):
    #status
    PREPARED = 0
    CONFIRMED = 1
    CANCELED = 2

    RESERVATION_STATUS = ((PREPARED, 'Prepared'),
                        (CONFIRMED, 'Confirmed'),
                        (CANCELED, 'Canceled'),)

    customer = models.ForeignKey(Customer, related_name='customer')
    inventory = models.ForeignKey(Rentalinventory, related_name='rentalinventory')
    in_date = models.DateTimeField(blank=True, null=False)
    out_date = models.DateTimeField(blank=True, null=False)
    status = models.IntegerField(null=False, choices=RESERVATION_STATUS)
    stock = models.PositiveIntegerField()

    class Meta:
        db_table = 'Reservation'
        ordering = ('in_date', 'status',) #정렬 1순위 in_date 2순위 상태

    def total_price(self):
        return self.stock * self.inventory.rentalproduct.price

    def save(self, *args, **kwargs):
        super(Reservation, self).save(*args, **kwargs) # Call the "real" save()

    def update(self, *args, **kwargs):
        print self.status, args, kwargs,'\n'

    def get_status(self):
        for i, v in self.RESERVATION_STATUS:
            if i is self.status:
                return v
