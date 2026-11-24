import datetime
from django.shortcuts import render

# Create your views here.
def flights(request, name ):
    now = datetime.datetime.now()
    return render(request, 'flights/index.html',{
        'date':now.month == 11 and now.day == 24,
        'name': name.capitalize(),
    })