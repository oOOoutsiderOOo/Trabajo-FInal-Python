from django.shortcuts import render
from django.http import HttpResponse
from users.models import User
from users.forms import EditPicForm

from posts.models import Post

def index(request):
    posts = Post.objects.all()
    profile_pic_form = EditPicForm()
    uid = request.COOKIES.get('user_id')
    user = User.objects.get(id=uid)
    
    for post in posts:
        post.body = post.body[:200] + "..."
        
    return render(request, 'home.html', {'posts': posts, "user": user, 'profile_pic_form': profile_pic_form})
