from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('rental.urls', namespace='index')),
    url(r'^rental/', include('rental.urls', namespace='rental')),
    url(r'^address/', include('address.urls', namespace='address')),
    url(r'^cart/', include('Cart.urls', namespace='cart')),
    url(r'^account/', include('account.urls', namespace='account')),
    url(r'^markdownx/', include('markdownx.urls')),
    url(r'^lecture/', include('lecture.urls', namespace='lecture')),
]

#if django is develop mode ...
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
