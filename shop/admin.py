from django.contrib import admin

from .models import Store

class StoreAdmin(admin.ModelAdmin):
    list_display = ['id','address', 'name']

admin.site.register(Store, StoreAdmin)

from django.contrib.sessions.models import Session
class SessionAdmin(admin.ModelAdmin):
    def _session_data(self, obj):
        return obj.get_decoded()
    list_display = ['session_key', '_session_data', 'expire_date']
admin.site.register(Session, SessionAdmin)
