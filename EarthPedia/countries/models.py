from django.db import models


class Country(models.Model):
    name_common = models.CharField(max_length=100, primary_key=True)
    name_official = models.CharField(max_length=255)
    native_name = models.TextField(blank=True, null=True)  
    capital = models.CharField(max_length=100, blank=True, null=True)
    region = models.CharField(max_length=100)
    subregion = models.CharField(max_length=100, blank=True, null=True)
    population = models.BigIntegerField()
    area = models.FloatField()
    flag_url = models.URLField(blank=True, null=True)
    coat_of_arms_url = models.URLField(blank=True, null=True)
    cca2 = models.CharField(max_length=3)
    cca3 = models.CharField(max_length=3)
    cioc = models.CharField(max_length=3, blank=True, null=True)
    fifa = models.CharField(max_length=3, blank=True, null=True)
    timezones = models.CharField(max_length=200)
    independent = models.BooleanField(default=False)
    un_member = models.BooleanField(default=False)
    start_of_week = models.CharField(max_length=20, blank=True, null=True)
    landlocked = models.BooleanField(default=False)
    tld = models.CharField(max_length=100, blank=True, null=True)
    alt_spellings = models.TextField(blank=True, null=True)  
    borders = models.TextField(blank=True, null=True)  
    languages = models.TextField(blank=True, null=True)  
    