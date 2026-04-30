from django.contrib import admin
from .models import Brand, Country, CarModel

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    # Просто виводимо ціну як є, вона вже буде з ($) у заголовку
    list_display = ('name', 'brand', 'price', 'created_at', 'updated_at')

admin.site.register(Brand)
admin.site.register(Country)