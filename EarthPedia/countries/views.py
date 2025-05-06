from django.shortcuts import render
from django.http import HttpResponse
from countries.models import Country

# Create your views here.
def index(request):
    countries = Country.objects.all()
    return render(request, 'index.html', {'countries': countries})

def country_details(request, name):
    country = Country.objects.get(name_common=name)
    return render(request, 'country_details.html', {'country': country})