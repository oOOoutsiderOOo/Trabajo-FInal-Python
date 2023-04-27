from django.http import HttpResponse
from django.shortcuts import render

from users.models import User

from .forms import NewPostForm
from .models import Post


#Views----------------------------------------------
def newPostView(request):
    form = NewPostForm()
    return render(request, 'newPost.html', {"form":form})

#API------------------------------------------------

def newPost(request):
    form = NewPostForm(request.POST)
    if form.is_valid():
        title = form.cleaned_data['title']
        body = form.cleaned_data['body']
        user_id = request.COOKIES.get('user_id')
        user = User.objects.get(id=user_id)
        post = Post(title=title, body=body, author=user)
        post.save()
        return HttpResponse("Success")
