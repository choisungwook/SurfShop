from django.conf.urls import url
import views

urlpatterns = [
    url(r'^search/$', views.searchRentalProduct.as_view(), name='rentalsearch'),
]