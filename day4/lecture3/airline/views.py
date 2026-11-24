from django.http import HttpResponse
from django.shortcuts import render

def airline_name(request):
    return render(request, 'welcome/index.html')

def airline_location(request):
    return HttpResponse('Jomo kenyatta Airport.')

def airline_summary(request, name, location='Jomo kenyatta', depature='1200H'):
    return HttpResponse(f'The airline is {name}<br>'
                        f'Depature time: {depature}<br>'
                        f'Location: {location}')

def person_details(request, name):
    return render(request, 'welcome/person.html',{
         'name': name.capitalize()
    }
                  )