import requests
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Fetches country data from the REST Countries API'

    def handle(self, *args, **options):
        api_url = 'https://restcountries.com/v3.1/all'
        response = requests.get(api_url)
        countries_data = response.json()

        print(countries_data[:1])