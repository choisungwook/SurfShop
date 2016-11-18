from django.contrib import admin
from .models import Customer

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'image', 'address']

admin.site.register(Customer, ProfileAdmin)
