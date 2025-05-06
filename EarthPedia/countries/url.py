from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('country_details/<str:name>', views.country_details, name='country_details'),
    path('Add_country', views.Add_country, name='Add_country'),
    path('Delete_country/<str:name>', views.Delete_country, name='Delete_country'),
    path('Update_country/<str:name>', views.Update_country, name='Update_country'),
]