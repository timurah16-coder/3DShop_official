from django.contrib import admin
from .models import Model3D, Order

@admin.register(Model3D)
class Model3DAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'image_preview']
    readonly_fields = ['image_preview']

    def image_preview(self, obj):
        if obj.image_name:
            return f'<img src="{obj.image_url()}" style="max-height:100px;"/>'
        return "—"
    image_preview.short_description = "Превью"
    image_preview.allow_tags = True  # ← Важно! Разрешает HTML

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'model', 'color', 'pickup_date', 'created_at']
    list_filter = ['model', 'created_at']
    readonly_fields = ['created_at']