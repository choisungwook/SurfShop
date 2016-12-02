from django.contrib import admin
from .models import RentalCategory, RentalProduct, Rentalinventory, Reservation

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(RentalCategory, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock',
                    'available', 'published', 'last_update']
    list_filter = ['available', 'published', 'last_update']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(RentalProduct, ProductAdmin)

class RentalinventoryAdmin(admin.ModelAdmin):
    list_display = ['store', 'rentalproduct']
admin.site.register(Rentalinventory, RentalinventoryAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = ['customer', 'inventory', 'in_date', 'out_date',
                    'status', 'stock']
    list_editable = ['status', 'stock']
    list_filter = ['customer', 'status']
admin.site.register(Reservation, ReservationAdmin)
