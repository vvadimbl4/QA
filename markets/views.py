from django.shortcuts import render

from .models import Location, Product


def location_list(request):
    locations = Location.objects.all()
    return render(request, 'markets/location_list.html', {'locations': locations})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'markets/product_list.html', {'products': products})
