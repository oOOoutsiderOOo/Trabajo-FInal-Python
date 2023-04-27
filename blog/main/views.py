from django.shortcuts import render
from django.http import HttpResponse

from posts.models import Post

def index(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})
