from django.conf.urls import url
import views

urlpatterns = [
    url(r'^index', views.indexView, name='index'),
    url(r'^login', views.loginView, name='login'),
    url(r'^logout', views.logoutView, name='logout'),
    url(r'^mypage', views.mypage, name='mypage'),
    url(r'^profile', views.profile, name='profile'),
    url(r'^register', views.register, name='register'),
]
