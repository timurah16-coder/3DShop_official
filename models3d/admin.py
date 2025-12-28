from django.contrib import admin
from .models import Model3D, Order

@admin.register(Model3D)
class Model3DAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'description']
    search_fields = ['name']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'model', 'color', 'pickup_date', 'created_at']
    list_filter = ['model', 'created_at']
    readonly_fields = ['created_at']