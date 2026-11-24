from django.urls import path
from . import views

urlpatterns = [
    path('tasks/<str:name>/<int:phoneNumber>/', views.tasks, name='tasks'),
    path('add/<str:name>/<int:phoneNumber>/', views.addtask, name='add')

]