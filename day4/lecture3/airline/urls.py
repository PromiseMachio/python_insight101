from django.urls import path
from . import views

urlpatterns = [
    path('', views.airline_name, name='name'),
    path('location/', views.airline_location, name='location'),
    path('summary/<str:name>/', views.airline_summary, name='summary'),
    path('person/<str:name>/', views.person_details, name='person')
]