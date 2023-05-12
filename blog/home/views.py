from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import Q
from users.models import User
from users.forms import EditPicForm
from .forms import SearchForm

from posts.models import Post

def index(request):
    profile_pic_form = EditPicForm()
    search_form = SearchForm()
    
    #intenta recuperar el uid del token de acceso, si no lo consigue redirige a login
    uid = User.get_uid_from_token(request.COOKIES.get('access_token'))
    if not uid: 
        response = HttpResponseRedirect("/login/")
        response.delete_cookie('access_token')
        return response
    user = User.objects.get(id=uid)
    
    #chequea si existe una busqueda en la url, luego trae los posts de la bd y los recorta a 200 caracteres
    #la búsqueda es en el título y en el cuerpo del post
    search_string = request.GET.get('search')
    
    if search_string:
        posts = Post.objects.filter(Q(title__icontains = search_string) | Q(body__icontains = search_string))
    else :
        posts = Post.objects.all()
        
    for post in posts:
        post.body = post.body[:200] + "..."
        
    context = {'posts': posts, "user": user, 'profile_pic_form': profile_pic_form, 'search_form': search_form}
        
    return render(request, 'home.html', context)

#API ------------------------------------------------

def search(request):
    search_form = SearchForm(request.POST)
    if search_form.is_valid():
        search_string = search_form.cleaned_data['search']
        return HttpResponseRedirect("/?search=" + search_string)
