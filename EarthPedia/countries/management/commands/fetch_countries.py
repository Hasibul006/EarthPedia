from django.core.management.base import BaseCommand
from countries.models import Country 
import requests

class Command(BaseCommand):
    help = 'Fetches country data from an external API and saves it to the database'

    def handle(self, *args, **kwargs):
        # Fetch data from the API
        url = "https://restcountries.com/v3.1/all"
        response = requests.get(url)

        if response.status_code == 200:
            countries_data = response.json()

            for country_data in countries_data:
                # Extracting country information from API response
                country_name_common = country_data.get('name', {}).get('common', 'Unknown')
                country_name_official = country_data.get('name', {}).get('official', 'Unknown')
                native_name = country_data.get('translations', {}).get('eng', {}).get('common', 'Unknown')
                capital = country_data.get('capital', ['Unknown'])[0]
                region = country_data.get('region', 'Unknown')
                subregion = country_data.get('subregion', 'Unknown')
                population = country_data.get('population', 0)
                area = country_data.get('area', 0.0)
                flag_url = country_data.get('flags', {}).get('png', '')
                cca2 = country_data.get('cca2', '')
                cca3 = country_data.get('cca3', '')
                cioc = country_data.get('cioc', '')
                fifa = country_data.get('fifa', '')
                coat_of_arms_url = country_data.get('coatOfArms', {}).get('png', '')
                timezones = ', '.join(country_data.get('timezones', []))
                independent = country_data.get('independent', False)
                un_member = country_data.get('unMember', False)
                start_of_week = country_data.get('startOfWeek', '')
                landlocked = country_data.get('landlocked', False)
                tld = ', '.join(country_data.get('tld', []))
                alt_spellings = ', '.join(country_data.get('altSpellings', []))
                borders = ', '.join(country_data.get('borders', []))

                # Saving the data to the Country model
                if not Country.objects.filter(name_common=country_name_common).exists():
                    Country.objects.create(
                        name_common=country_name_common,
                        name_official=country_name_official,
                        native_name=native_name,
                        capital=capital,
                        region=region,
                        subregion=subregion,
                        population=population,
                        area=area,
                        flag_url=flag_url,
                        cca2=cca2,
                        cca3=cca3,
                        cioc=cioc,
                        fifa=fifa,
                        timezones=timezones,
                        independent=independent,
                        un_member=un_member,
                        start_of_week=start_of_week,
                        landlocked=landlocked,
                        coat_of_arms_url=coat_of_arms_url,
                        tld=tld,
                        alt_spellings=alt_spellings,
                        borders=borders
                    )
                else:
                    self.stdout.write(self.style.WARNING(f'Country {country_name_common} already exists in the database'))
                    continue
            self.stdout.write(self.style.SUCCESS('Successfully fetched and saved country data to the database'))
        else:
            self.stdout.write(self.style.ERROR('Failed to fetch country data'))
