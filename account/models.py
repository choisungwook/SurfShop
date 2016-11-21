from __future__ import unicode_literals

from django.db import models
from django.conf import settings
from address.models import Address
from django.utils.encoding import force_unicode
import os.path

class Customer(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, unique=True)
    image = models.ImageField(upload_to=lambda instance, filename:'customers/{0}.jpg'.format(instance.user.id), blank=True )

    address = models.ForeignKey(Address)

    class Meta:
        db_table = 'customer'


    def __unicode__(self):
        return self.user.username

