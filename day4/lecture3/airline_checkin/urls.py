from django.urls import path
from . import views

urlpatterns =[
    path('checkin/', views.airline_checkin, name='checkin'),
    path('add/', views.add_checkins, name='addCheckin')
]