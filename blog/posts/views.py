from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from users.forms import EditPicForm

from users.models import User

from comments.forms import NewCommentForm, DeleteCommentForm
from comments.models import Comment

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
    comments = Comment.objects.filter(post_id=id)
    new_comment_form = NewCommentForm()
    delete_comment_form = DeleteCommentForm()
    return render(request, 'article.html', {"post":post,
                                            "user_id":user_id,
                                            "user":user,
                                            "new_comment_form":new_comment_form,
                                            "comments":comments,
                                            "delete_comment_form":delete_comment_form })

#API------------------------------------------------

def newPost(request):
    form = NewPostForm(request.POST, request.FILES)
    if form.is_valid():
        title = form.cleaned_data['title']
        body = form.cleaned_data['body']
        image = form.cleaned_data['image']
        user_id = request.COOKIES.get('user_id')
        user = User.objects.get(id=user_id)
        post = Post(title=title, body=body, author=user, image=image)
        post.save()
        return HttpResponseRedirect('/')
    
def editPost(request):
    try:
        form = EditPostForm(request.POST, request.FILES)

        if form.is_valid():
            post = Post.objects.get(id=form.cleaned_data['id'])
            
            title = form.cleaned_data['title']
            body = form.cleaned_data['body']
            print(form.cleaned_data['image'])
            if form.cleaned_data['image']:
                image = form.cleaned_data['image']
                post.image = image
                print("imagen cambiada")
            
            post.title = title
            post.body = body
            post.save()
            return HttpResponseRedirect('/')
    
    except Exception as e:
        print("error " + e)
        return HttpResponse("error " + e)
    
#TODO refactorizar para usar un formulario
def deletePost(request):
    id = request.GET.get('id')
    post = Post.objects.get(id=id)
    post.delete()
    return HttpResponseRedirect('/')
