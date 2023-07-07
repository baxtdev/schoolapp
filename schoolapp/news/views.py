from django.shortcuts import redirect, render
from django.db import models
from news.models import *
from django.views import generic
from .forms import CommentsForm

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
    s_news = New.objects.get(id=pk)
    comments = Comments.objects.all()
    if request.method == "POST":  
        form = CommentsForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save() 
                model = form.instance
                return redirect('single_news')  
            except:  
                pass  
    else:  
        form = CommentsForm()     
    context = {'s_new': s_news, 'form': form,'coments':comments}
    
    return render(request, 'single_news.html', context)


    
