from __future__ import unicode_literals

from django.db import models

class Sido(models.Model):
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'sido'

    def __str__(self):
        return self.name.encode('ascii', errors='replace')

class Sigungu(models.Model):
    sido = models.ForeignKey(Sido, related_name='sido_id')
    name = models.CharField(max_length=45)

    class Meta:
        db_table = 'sigungu'

    def __str__(self):
        return self.name.encode('ascii', errors='replace')


