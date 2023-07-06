from django.shortcuts import render
from quiz.models import Quiz


# Create your views here.
def quiz(request):
    questions = Quiz.objects.all()

    return render(request, 'quiz.html', {'questions': questions})
