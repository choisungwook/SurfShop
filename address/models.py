from __future__ import unicode_literals

from django.db import models

class Sido(models.Model):
    name = models.CharField(max_length=45, unique=True)

    class Meta:
        db_table = 'sido'

    def __unicode__(self):
        return self.name

class Sigungu(models.Model):
    sido = models.ForeignKey(Sido, related_name='sido_id')
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'sigungu'

    def __unicode__(self):
        return self.name

class Address(models.Model):
    Sigungu = models.ForeignKey(Sigungu, related_name='Sigungu')
    other_address = models.CharField(max_length=100, blank=True, null=False)
    phone = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        db_table = 'address'

    def __unicode__(self):
        return self.Sigungu.sido.name + ' ' + self.Sigungu.name
