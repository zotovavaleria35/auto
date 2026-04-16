from django.db import models


# 1. Таблиця Країна
class Country(models.Model):
    name = models.CharField(max_length=50, verbose_name="Країна")

    def __str__(self):
        return self.name


# 2. Таблиця Марка
class Brand(models.Model):
    name = models.CharField(max_length=50, verbose_name="Марка")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Країна")

    def __str__(self):
        return self.name


# 3. Таблиця Модель (Об'єднуємо тут)
class CarModel(models.Model):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, verbose_name="Марка")
    name = models.CharField(max_length=50, verbose_name="Назва моделі")

    # Поля для лаби
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Створено о")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Оновлено о")

    def __str__(self):
        return self.name