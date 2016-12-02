from django.conf.urls import url
import views

urlpatterns = [
    url(r'^$', views.listtAll, name='all'),
    url(r'^list/(?P<subject>\d+)/$', views.lectureListView.as_view(), name='list'),
]
