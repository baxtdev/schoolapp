from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('list_lesson', views.raspisanie, name='list-lessons'),
    path('students/<int:pk>', views.studentlist, name='students'),
    # path('students2/', views.studentlist2, name='students2'),
    path('student/<int:pk>/', views.studentdetail, name='student'),
    path('teachers/', views.teachers, name='teachers'),
    path('courses/', views.courses, name='courses'),
    path('contact/', views.contact, name='contact'),
    path('header/', views.header, name='header'),

]