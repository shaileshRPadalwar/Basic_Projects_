from django.contrib import admin
from .models import StudentRegistration
# Register your models here.
@admin.register(StudentRegistration)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'marks']

