from django.shortcuts import render
from .models import Post
from django.views.generic import ListView

#Function based views
def home(request):
    context = {
        'posts' : Post.objects.all()
    }
    return render(request,'blog/home.html', context)

#Class based views
class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})