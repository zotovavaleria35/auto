from django.contrib import admin
from .models import Brand, Country, CarModel # Імпортуємо тільки те, що є в models.py

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    # Виводимо назву моделі, марку та дати
    list_display = ('name', 'brand', 'created_at', 'updated_at')

admin.site.register(Brand)
admin.site.register(Country)