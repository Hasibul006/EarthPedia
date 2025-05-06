from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country_details/<str:name>', views.country_details, name='country_details'),
]