from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from users.forms import EditPicForm

from users.models import User

from .forms import EditPostForm, NewPostForm
from .models import Post


#Views----------------------------------------------

def newPostView(request):
    form = NewPostForm()
    profile_pic_form = EditPicForm()
    user_id = request.COOKIES.get('user_id')
    user = User.objects.get(id=user_id)
    return render(request, 'newPost.html', {"form":form, "user":user,'profile_pic_form': profile_pic_form})

def editPostView(request):
    post = Post.objects.get(id=request.GET.get('id'))
    initial = {'id': post.id, 'title': post.title, 'body': post.body}
    form = EditPostForm(initial=initial)
    profile_pic_form = EditPicForm()
    user_id = request.COOKIES.get('user_id')
    user = User.objects.get(id=user_id)
    return render(request, 'editPost.html', {"form":form, "user":user,'profile_pic_form': profile_pic_form})

def articleView(request):
    id = request.GET.get('id')
    post = Post.objects.get(id=id)
    user_id = int(request.COOKIES.get('user_id'))
    user = User.objects.get(id=user_id)
    return render(request, 'article.html', {"post":post, "user_id":user_id, "user":user })

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
        return HttpResponseRedirect('/')
    
def editPost(request):
    try:
        form = EditPostForm(request.POST)
        print(form.base_fields.values())
        if form.is_valid():
            post = Post.objects.get(id=form.cleaned_data['id'])
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            post.title = title
            post.body = body
            post.save()
            return HttpResponseRedirect('/')
    except Exception as e:
        print("error " + e)
        return HttpResponse("error " + e)
    
def deletePost(request):
    id = request.GET.get('id')
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect('/')
