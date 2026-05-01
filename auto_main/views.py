from django.shortcuts import render, get_object_or_404
from .models import Brand, CarModel

def home(request):
    brands = Brand.objects.all()
    return render(request, 'index.html', {'brands': brands})

def catalog(request):
    brands = Brand.objects.all()
    cars = CarModel.objects.all()
    return render(request, 'catalog.html', {'cars': cars, 'brands': brands})

def brand_filter(request, brand_id):
    brands = Brand.objects.all()
    brand = get_object_or_404(Brand, id=brand_id)
    cars = CarModel.objects.filter(brand=brand)
    return render(request, 'catalog.html', {'cars': cars, 'brands': brands, 'selected_brand': brand})

def car_detail(request, car_id):
    brands = Brand.objects.all()
    # Отримуємо конкретну модель авто за ID
    car = get_object_or_404(CarModel, id=car_id)
    return render(request, 'car_detail.html', {'car': car, 'brands': brands})

def about(request):
    brands = Brand.objects.all()
    return render(request, 'about.html', {'brands': brands})

def contacts(request):
    brands = Brand.objects.all()
    return render(request, 'contacts.html', {'brands': brands})