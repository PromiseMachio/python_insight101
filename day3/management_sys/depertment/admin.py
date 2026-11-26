from django.contrib import admin

from .models import Depertment, Employee, Institution
# Register your models here.
class DepertmentAdmin(admin.ModelAdmin):
    list_display = ('id','name','depertment_code','phone_number')

class EmployeeAdmin(admin.ModelAdmin):
    filter_horizontal = ('depertment',)

admin.site.register(Institution)
admin.site.register(Depertment, DepertmentAdmin)
admin.site.register(Employee, EmployeeAdmin)