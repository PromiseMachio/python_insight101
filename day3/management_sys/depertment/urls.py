from django.urls import path
from . import views

urlpatterns = [
    path('zip1/', views.view_depertments, name='depertments'),
    path('zip2/', views.view_employees, name='employess'),
    path('zip3/<int:depertment_id>/', views.in_dept, name='single_dpt'),
    path('zip4/<int:department_id>/', views.add_employee, name='add_employee')

]