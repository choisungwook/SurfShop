from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login', views.loginView, name='login'),
    url(r'^logout', views.logoutView, name='logout'),
    url(r'^mypage', views.mypage, name='mypage'),
    url(r'^register', views.register, name='register'),
]
