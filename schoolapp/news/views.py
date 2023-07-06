from django.shortcuts import render
from django.db import models
from news.models import *
from django.views import generic


# Create your views here.


#home page


# news page
# class NewListView(generic.ListView):
#     queryset = New.objects.all()
#     model = New
#     template_name = 'news/i.html'
#     context_object_name = 'news'
#
#     def get_queryset(self):
#         return New.objects.all()


def news(request):
    model = New
    posts = model.objects.all()
    return render(request,'news.html', {'posts': posts} )


#
# class NewDetailView(generic.DetailView):
#
#     model = New
#     template_name = 'news/simple_post.html'
#     context_object_name = 'news'
#
#     def get_objects(self):
#         obj = super().get_object()
#         obj.news_view += 1
#         obj.save()
#         return obj
#

def single_news(request, pk):
    model = New
    s_news = model.objects.get(id=pk)
    return render(request, 'single_news.html', {'s_new': s_news})

