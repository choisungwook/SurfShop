# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.apps import AppConfig

class RentalConfig(AppConfig):
    name = 'rental'
    verbose_name = "렌탈 관련부분"
    def ready( self ):
        from rental.signals import pre_save_Reservation
