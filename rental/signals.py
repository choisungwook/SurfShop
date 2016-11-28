# -*- encoding:utf-8 -*-
from django.db.models.signals import pre_save, post_save
from django.dispatch  import receiver
from .views import Reservation
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
from django.contrib.auth.models import User

@receiver(pre_save, sender=Reservation)
def pre_save_Reservation(sender, **kwargs):
    instance = kwargs['instance']

    try:
        obj = sender.objects.get(pk=instance.pk)
        user = User.objects.get(pk=instance.customer.user.id)

        title = "예약확인 확인되었습니다"
        body = "예약확인 확인되었습니다"
        to = user.email

        if obj.status is 0 and instance.status is 1:
            send_mail(title, body, 'csw19591@gmail.com', ['보낼메일'], fail_silently=False)
    except sender.DoesNotExist: #발견이 안되면 새로 만드는 경우이다.
        pass
