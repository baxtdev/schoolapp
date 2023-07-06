from django.contrib import admin
from .models import Student, Teachers, Courses, List

class Studentlist(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'l_class', 'phone_number')

# Register your models here.
admin.site.register(Student,Studentlist),
admin.site.register(Teachers)
admin.site.register(Courses)
admin.site.register(List)