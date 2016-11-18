from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from address.models import Address

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    image = models.ImageField(upload_to='/customers', blank=True)
    address = models.ForeignKey(Address)

    class Meta:
        db_table = 'customer'

