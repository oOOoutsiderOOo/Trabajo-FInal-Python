from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from .models import Comment
from .forms import NewCommentForm
from users.models import User
from posts.models import Post

#API--------------------------------------------------------

def createComment(request):
    """ Recibe un POST con los datos de un comentario y lo crea en la base de datos. Si es una respuesta 
    se incluye el id del comentario al que responde."""
    
    form = NewCommentForm(request.POST)
    if request.method == 'POST' and  form.is_valid():
        try:
            user_id = form.cleaned_data['user_id']
            user = User.objects.get(id=user_id)
            post_id = form.cleaned_data['post_id']
            post = Post.objects.get(id=post_id)
            content = form.cleaned_data['content']
            
            if request.POST.get('response_to_id'):
                response_to_id = form.cleaned_data['response_to_id']
                response_to = Comment.objects.get(id=response_to_id)
                is_response = True
                comment = Comment(user=user, post=post, response_to=response_to, content=content, is_response=is_response)
            else:
                comment = Comment(user=user, post=post, content=content)
                
            comment.save()
            return HttpResponseRedirect('/article/?id='+str(post_id))
        
        except Exception as e:
            return HttpResponse(e)
    
    else:
        return HttpResponse(status=400)
