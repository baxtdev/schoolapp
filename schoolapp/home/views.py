from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render
from news.models import *
from home.models import *

from .forms import ContactForm


# Create your views here.

def home(request):
    popular = PopularStudents.objects.all()
    return render(request, 'home.html', {'popular':popular})

#
# def studentlist(request, post):
#     post = get_object_or_404(Student, id=post, status='student')
#     return render(request, 'students.html', {'student': post})


def studentlist(request, pk):
    students = Student.objects.all()
    return render(request, 'students.html', {'students': students})


def studentdetail(request, pk):
    student = Student.objects.get(id=pk)
    return render(request, 'student.html', {'student': student})


def teachers(request):
    teacher = Teachers.objects.all()
    return render(request, 'teachers.html', {'teacher': teacher})

def course_detail(request,pk):
    courses = Courses.objects.get(id=pk)
    return render(request, )

def courses(request):
    course = Courses.objects.all()
    return render(request, 'courses.html', {'course': course})


def contact(request):
    contacts = Contact.objects.all()
    schole = Schole.objects.all()
    
    if request.method == "POST":  
        form = ContactForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('contact')  
            except:  
                pass  
    else:  
        form = ContactForm()  

    context = {'contacts': contacts,'form':form, 'schole':schole}
    return render(request, 'contact.html', context)


def header(request):
    return render(request, 'header.html')

def raspisanie(request):
    return render(request,'raspis.html')

def detail_class(request, id):
    class_item = List.objects.get(id=id)
    student= Student.objects.all()
    return render(request, 'classes.html', {'class_item': class_item,'students':student,})
