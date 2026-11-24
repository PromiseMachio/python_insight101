from django.shortcuts import render
from django import forms
from django.http import HttpResponseRedirect
from django.urls import reverse


# Create your views here.
task_items = [
    {'title': 'Confirm flight', 'priority': 1},
    {'title': 'Book online', 'priority': 2},
    {'title': 'Add checked luggage', 'priority': 3},
    {'title': 'Pack travel documents', 'priority': 4},
    {'title': 'Arrive at the airport', 'priority': 5},
    {'title': 'Proceed to boarding gate', 'priority': 6},
]
class NewTaskForm(forms.Form):
    tasks = forms.CharField(label='New Task')
    priority = forms.IntegerField(label='Priority', min_value=1, max_value=10)


def tasks(request,name,phoneNumber):
    return render(request, 'tasks/index.html',{
        'tasks':task_items,
        'name': name,
        'phoneNumber': phoneNumber
       
        
    })

def addtask(request,name, phoneNumber):
    if request.method == 'POST':
        # process the result of that form 
        form = NewTaskForm(request.POST)  # return that variable that way will render a page users data
        if form.is_valid():
            task = form.cleaned_data['tasks'] 
            task_items.append(task)
            return HttpResponseRedirect(reverse('tasks',
                                                kwargs={
                                                    'name':name,
                                                    'phoneNumber':phoneNumber
                                                }))
        else:
            return render(request, 'tasks/add.html',{
                'form':form
            })
    return render(request, 'tasks/add.html',{
        'form':NewTaskForm(),
        'name':name,
        'phoneNumber':phoneNumber
    })
