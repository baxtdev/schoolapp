from django.shortcuts import get_object_or_404
from django.shortcuts import render
from news.models import *
from home.models import *


# Create your views here.

def home(request):
    return render(request, 'home.html')

#
# def studentlist(request, post):
#     post = get_object_or_404(Student, id=post, status='student')
#     return render(request, 'students.html', {'student': post})


def studentlist(request):
    students = Student.objects.filter(l_class=1)
    return render(request, 'students.html', {'students': students})

def studentlist2(request):
    students2 = Student.objects.filter(l_class=2)
    return render(request, 'students2.html', {'students2': students2})


def studentdetail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'student.html', {'student': student})


def teachers(request):
    teacher = Teachers.objects.all()
    return render(request, 'teachers.html', {'teacher': teacher})


def courses(request):
    course = Courses.objects.all()
    return render(request, 'courses.html', {'course': course})


def contact(request):
    return render(request, 'contact.html')


def header(request):
    return render(request, 'header.html')

def raspisanie(request):
    return render(request,'raspis.html')

def detail_class(request, id):
    class_item = List.objects.get(id=id)
    student= Student.objects.all()
    return render(request, 'classes.html', {'class_item': class_item,'students':student,})
