from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.searchRentalProduct),
    url(r'^search/$', views.searchRentalProduct, name='rentalsearch'),
    url(r'^list/$', views.list_storeRentalProduct, name='rentallist'),
    url(r'^detail/(?P<inventory_id>\d+)/$', views.detail_RentalProduct, name='detail'),
    url(r'^reservation/$', views.make_reservation, name='reservation'),
    url(r'^cancel/(?P<reservation_id>\d+)/$', views.cancel_reservation, name='cancel'),
]
