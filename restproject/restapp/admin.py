from django.contrib import admin
from .models import Student, Student1


# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city']


@admin.register(Student1)
class Student1Admin(admin.ModelAdmin):
    list_display = ['id', 'name', 'roll', 'city', 'passby']
