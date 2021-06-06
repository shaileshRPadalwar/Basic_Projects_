from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['ename','enum','esal']

#admin.site.register(Employee,EmployeeAdmin)
