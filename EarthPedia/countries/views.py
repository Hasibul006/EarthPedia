from django.shortcuts import render,redirect
from django.http import HttpResponse
from countries.models import Country

# Create your views here.
def index(request):
    countries = Country.objects.all()
    return render(request, 'index.html', {'countries': countries})

def country_details(request, name):
    country = Country.objects.get(name_common=name)
    return render(request, 'country_details.html', {'country': country})

def Delete_country(request, name):
        country = Country.objects.get(name_common=name)
        country.delete()
        return redirect('/')

def Add_country(request):
    if request.method == 'POST':
        name_common=request.POST.get('name_common'),
        name_official=request.POST.get('name_official'),
        native_name=request.POST.get('native_name', ''),
        capital=request.POST.get('capital', None),
        region=request.POST.get('region'),
        subregion=request.POST.get('subregion', None),
        population=int(request.POST.get('population')),
        area=float(request.POST.get('area')),
        flag_url=request.POST.get('flag_url', None),
        coat_of_arms_url=request.POST.get('coat_of_arms_url', None),
        cca2=request.POST.get('cca2'),
        cca3=request.POST.get('cca3'),
        cioc=request.POST.get('cioc', None),
        fifa=request.POST.get('fifa', None),
        timezones=request.POST.get('timezones'),
        independent=request.POST.get('independent') == 'on',
        un_member=request.POST.get('un_member') == 'on',
        start_of_week=request.POST.get('start_of_week', None),
        landlocked=request.POST.get('landlocked') == 'on',
        tld=request.POST.get('tld', None),
        alt_spellings=request.POST.get('alt_spellings', None),
        borders=request.POST.get('borders', None)

        if Country.objects.filter(name_common=name_common).exists():
            print("Country already exists in database")
            return redirect('/Add_country')
        else:
            country = Country(
                name_common=request.POST.get('name_common'),
                name_official=request.POST.get('name_official'),
                native_name=request.POST.get('native_name', ''),
                capital=request.POST.get('capital', None),
                region=request.POST.get('region'),
                subregion=request.POST.get('subregion', None),
                population=int(request.POST.get('population')),
                area=float(request.POST.get('area')),
                flag_url=request.POST.get('flag_url', None),
                coat_of_arms_url=request.POST.get('coat_of_arms_url', None),
                cca2=request.POST.get('cca2'),
                cca3=request.POST.get('cca3'),
                cioc=request.POST.get('cioc', None),
                fifa=request.POST.get('fifa', None),
                timezones=request.POST.get('timezones'),
                independent=request.POST.get('independent') == 'on',
                un_member=request.POST.get('un_member') == 'on',
                start_of_week=request.POST.get('start_of_week', None),
                landlocked=request.POST.get('landlocked') == 'on',
                tld=request.POST.get('tld', None),
                alt_spellings=request.POST.get('alt_spellings', None),
                borders=request.POST.get('borders', None)
            )
        country.save()
        return redirect('/')
    return render(request, 'Add_country.html')
    
    