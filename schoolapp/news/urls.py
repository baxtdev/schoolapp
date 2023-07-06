from django.urls import path
from . import views


urlpatterns = [
    path('', views.news, name='news'),
    path('single_news/<int:pk>/', views.single_news, name='single_news'),
]
