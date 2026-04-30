from django.db import models

class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name="Країна")
    def __str__(self): return self.name

class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name="Марка")
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    def __str__(self): return self.name

class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Марка")
    name = models.CharField(max_length=50, verbose_name="Назва моделі")
    # Додали ($) в назву поля
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Ціна ($)")
    description = models.TextField(default='', verbose_name="Опис")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self): return self.name