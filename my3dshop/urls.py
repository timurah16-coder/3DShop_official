from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('models3d.urls')),
    path('order/<int:model_id>/', views.order, name='order'),
    path('success/', views.success, name='success'),  # ← ЭТО ДОЛЖНО БЫТЬ!
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)