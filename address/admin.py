from django.contrib import admin
from .models import Address, Sigungu, Sido

class SidoAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Sido, SidoAdmin)

class SigunguAdmin(admin.ModelAdmin):
    list_display = ['sido', 'name']
admin.site.register(Sigungu, SigunguAdmin)

class AddressAdmin(admin.ModelAdmin):
    list_display = ['Sigungu', 'other_address', 'phone']

admin.site.register(Address, AddressAdmin)