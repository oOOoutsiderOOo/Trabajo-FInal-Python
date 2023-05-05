from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Comment
from .forms import NewCommentForm
from users.models import User
from posts.models import Post

#API--------------------------------------------------------

def createComment(request):
    form = NewCommentForm(request.POST)
    if request.method == 'POST' and  form.is_valid():
        try:
            
            print("form is valid")
            user_id = form.cleaned_data['user_id']
            user = User.objects.get(id=user_id)
            post_id = form.cleaned_data['post_id']
            post = Post.objects.get(id=post_id)
            content = form.cleaned_data['content']
            
            if request.POST.get('response_to_id'):
                response_to_id = form.cleaned_data['response_to_id']
                response_to = Comment.objects.get(id=response_to_id)
                is_response = True
                comment = Comment(user_id=user, post_id=post, response_to_id=response_to, content=content, is_response=is_response)
            else:
                comment = Comment(user_id=user, post_id=post, content=content)
                
            comment.save()
            return HttpResponse('Comment created')
        except Exception as e:
            return HttpResponse(e)
    
    else:
        return HttpResponse('Error', status=400)
