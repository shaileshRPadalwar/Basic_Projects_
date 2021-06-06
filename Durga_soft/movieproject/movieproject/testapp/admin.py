from django.contrib import admin
from .models import Movie
# Register your models here.
@admin.register(Movie)
class AdminMovie(admin.ModelAdmin):
    list_display=['rdate','moviename','hero','heroine','rating']

