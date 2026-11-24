from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
class AirlineCheckIn(forms.Form):
    checkIns = forms.CharField(label='Checkins')
    priority = forms.IntegerField(label='priority', min_value=1 ,max_value=10)

def airline_checkin(request):
    if 'checkins' not in request.session:
        request.session['checkins'] = []
    return render(request, 'checkin/index.html',{
        'checkins': request.session['checkins']
    })

def add_checkins(request):
    if request.method == 'POST':
        form = AirlineCheckIn(request.POST)
        if form.is_valid():
           checkin = form.cleaned_data['checkIns']
           request.session['checkins'] += [checkin]
           return HttpResponseRedirect(reverse('checkin'))
        else:
            return render(request, 'checkin/add.html', {'form': form})
    return render(request, 'checkin/add.html',{
        'form':AirlineCheckIn()
    })