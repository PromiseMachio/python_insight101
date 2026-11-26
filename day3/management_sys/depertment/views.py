from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Depertment, Employee
from django.urls import reverse

# Create your views here.
def view_depertments(request):
    return render(request, 'depertments/index.html',{
        'depertments': Depertment.objects.all()
    })
def view_employees(request):
    return render(request, 'depertments/employees.html',{
        'employees':Employee.objects.all()
    })
def in_dept(request, depertment_id):
    depertment= Depertment.objects.get(id=depertment_id)
    return render(request, 'depertments/depertment.html',{
        'depertments': depertment,
        'employees':depertment.employees.all(),
        'non_employees':Employee.objects.exclude(depertment=depertment).all()
    })

def add_employee(request, department_id):
    if request.method == 'POST':
        department = Depertment.objects.get(id=department_id)
        employee = Employee.objects.get(id=int(request.POST['employee']))
        employee.depertment.add(department)

        return HttpResponseRedirect(reverse('single_dpt', args=(department.id,)))


