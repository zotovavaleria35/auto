from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('catalog/', views.catalog, name='catalog'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    # Цей рядок обов'язковий для роботи меню марок
    path('brand/<int:brand_id>/', views.brand_filter, name='brand_filter'),

    # Додай цей рядок для сторінки товару
    path('car/<int:car_id>/', views.car_detail, name='car_detail'),
]