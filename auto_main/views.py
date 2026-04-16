from django.shortcuts import render

def home(request):
    return render(request, 'index.html', {'title': 'Головна'})

def other(request):
    return render(request, 'other.html', {'title': 'Інша сторінка'})