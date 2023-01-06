from django.shortcuts import render

posts = [
    {
        'author' : 'Matrix',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'Jan6 2023'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'Jan7 2023'
    }
]

# Create your views here.

def home(request):
    context = {
        'posts' : posts
    }
    return render(request,'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')