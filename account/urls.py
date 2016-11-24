from django.conf.urls import url
import views

urlpatterns = [
    url(r'^login', views.loginView, name='login'),
    url(r'^logout', views.logoutView, name='logout'),
]
