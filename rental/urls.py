from django.conf.urls import url
import views

urlpatterns = [
    url(r'^search/$', views.searchRentalProduct, name='rentalsearch'),
    url(r'^detail/(?P<inventory_id>\d+)/$', views.detail_RentalProduct, name='detail'),
    url(r'^reservation/$', views.make_reservation, name='reservation'),
]
