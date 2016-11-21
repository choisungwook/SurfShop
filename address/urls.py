from django.conf.urls import url
import views

urlpatterns = [
    url(r'^searchSigungu/$', views.searchSigungu, name='searchSigungu')
]
