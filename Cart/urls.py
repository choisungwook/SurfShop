from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.cart_detail, name='detail'),
    url(r'^add/(?P<inventory_id>\d+)/$', views.add_to_cart, name='add'),
    url(r'^remove/(?P<inventory_id>\d+)/$', views.remove_cartItem, name='remove'),
]
