from django.test import TestCase
from django.contrib.auth.models import User
from .models import Customer
from address.models import Sigungu, Address, Sido

class CustomerTestCase(TestCase):

    def setUp(self):
        # create user
        self.user = User.objects.create_user(username='aaa',
                                             email=None,
                                             password='bbbbbbbbbbb')

        self.sigungu = Sigungu.objects.get(id=1)

    def test_sigungu_can_read(self):
        self.assertIs(self.sigungu, False)




