from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('order/<int:model_id>/', views.order, name='order'),
    path('success/', views.success, name='success'),
]