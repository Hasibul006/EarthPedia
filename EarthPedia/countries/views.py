from django.shortcuts import render,redirect
from django.http import HttpResponse
from countries.models import Country

# Create your views here.
def index(request):
    # Prepare distinct region and language lists
    regions = Country.objects.exclude(region='').values_list('region', flat=True).distinct()
    language_values = Country.objects.exclude(languages='').values_list('languages', flat=True).distinct()

    # Extract unique languages from the text fields (comma-separated)
    all_languages = set()
    for entry in language_values:
        for lang in entry.split(','):
            lang = lang.strip()
            if lang:
                all_languages.add(lang)
    all_languages = sorted(all_languages)

    # Get filter values from GET request
    selected_region = request.GET.get('region')
    selected_language = request.GET.get('language')

    countries = Country.objects.all()

    if selected_region:
        countries = countries.filter(region=selected_region)
    if selected_language:
        countries = countries.filter(languages__icontains=selected_language)

    context = {
        'countries': countries,
        'regions': regions,
        'languages': all_languages,
        'selected_region': selected_region,
        'selected_language': selected_language,
    }
    return render(request, 'index.html', context)

def country_details(request, name):
    country = Country.objects.get(name_common=name)
    return render(request, 'country_details.html', {'country': country})

def Delete_country(request, name):
        country = Country.objects.get(name_common=name)
        country.delete()
        return redirect('/')

def Update_country(request, name):
        country = Country.objects.get(name_common=name)
        
        if request.method == 'POST':
            country.name_common=request.POST.get('name_common')
            country.name_official=request.POST.get('name_official')
            country.capital=request.POST.get('capital', None)
            country.region=request.POST.get('region')
            country.subregion=request.POST.get('subregion', None)
            country.population = int(request.POST.get('population'))
            country.area=float(request.POST.get('area'))
            country.languages=request.POST.get('languages', None)
            country.flag_url=request.POST.get('flag_url', None)
            country.coat_of_arms_url=request.POST.get('coat_of_arms_url', None)
            country.cca2=request.POST.get('cca2')
            country.cca3=request.POST.get('cca3')
            country.cioc=request.POST.get('cioc', None)
            country.fifa=request.POST.get('fifa', None)
            country.timezones=request.POST.get('timezones')
            country.independent=request.POST.get('independent') == 'on'
            country.un_member=request.POST.get('un_member') == 'on'
            country.start_of_week=request.POST.get('start_of_week', None)
            country.landlocked=request.POST.get('landlocked') == 'on'
            country.tld=request.POST.get('tld', None)
            country.alt_spellings=request.POST.get('alt_spellings', None)
            country.borders=request.POST.get('borders', None)
            country.save()
            return redirect('/')
        return render(request, 'Update_country.html', {'country': country})

def Add_country(request):
    if request.method == 'POST':
        name_common=request.POST.get('name_common')
        name_official=request.POST.get('name_official')
        capital=request.POST.get('capital', None)
        region=request.POST.get('region')
        subregion=request.POST.get('subregion', None)
        population=int(request.POST.get('population'))
        area=float(request.POST.get('area'))
        flag_url=request.POST.get('flag_url', None)
        coat_of_arms_url=request.POST.get('coat_of_arms_url', None)
        cca2=request.POST.get('cca2')
        cca3=request.POST.get('cca3')
        cioc=request.POST.get('cioc', None)
        fifa=request.POST.get('fifa', None)
        timezones=request.POST.get('timezones')
        independent=request.POST.get('independent') == 'on'
        un_member=request.POST.get('un_member') == 'on'
        start_of_week=request.POST.get('start_of_week', None)
        landlocked=request.POST.get('landlocked') == 'on'
        tld=request.POST.get('tld', None)
        alt_spellings=request.POST.get('alt_spellings', None)
        borders=request.POST.get('borders', None)
        languages=request.POST.get('languages', None)

        if Country.objects.filter(name_common=name_common).exists():
            print("Country already exists in database")
            return redirect('/Add_country')
        else:
            country = Country(
                name_common=name_common,
                name_official=name_official,
                capital=capital,
                region=region,
                subregion=subregion,
                population=int(population),
                area=float(area),
                languages=languages,
                flag_url=flag_url,
                coat_of_arms_url=coat_of_arms_url,
                cca2=cca2,
                cca3=cca3,
                cioc=cioc,
                fifa=  fifa,
                timezones=timezones,
                independent=independent,
                un_member=un_member,
                start_of_week=start_of_week,
                landlocked=landlocked,
                tld=tld,
                alt_spellings=alt_spellings,
                borders=borders
            )
        country.save()
        return redirect('/')
    return render(request, 'Add_country.html')

    