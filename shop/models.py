from __future__ import unicode_literals

from django.db import models
from address.models import Address

class Store(models.Model):
    address = models.ForeignKey(Address, related_name='address')
    name =  models.CharField(max_length=200, blank=True)

    def __unicode__(self):
        return self.name