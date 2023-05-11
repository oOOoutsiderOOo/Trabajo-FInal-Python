from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from users.models import User
from users.forms import EditPicForm

from posts.models import Post

def index(request):
    posts = Post.objects.all()
    profile_pic_form = EditPicForm()
    uid = User.get_uid_from_token(request.COOKIES.get('access_token'))
    if not uid: 
        response = HttpResponseRedirect("/login/")
        response.delete_cookie('access_token')
        return response
    user = User.objects.get(id=uid)
    
    for post in posts:
        post.body = post.body[:200] + "..."
        
    return render(request, 'home.html', {'posts': posts, "user": user, 'profile_pic_form': profile_pic_form})
