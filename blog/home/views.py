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
    page_number = request.GET.get('page')
    
    #cantidad de posts por página
    posts_per_page = 3
    
    #intenta recuperar el uid del token de acceso, si no lo consigue redirige a login
    uid = User.get_uid_from_token(request.COOKIES.get('access_token'))
    if not uid: 
        response = HttpResponseRedirect("/login/")
        response.delete_cookie('access_token')
        return response
    user = User.objects.get(id=uid)
    
    #chequea si existe una busqueda en la url, luego trae los posts de la bd y los recorta a 200 caracteres
    search_string = request.GET.get('search')     
    if search_string:
        posts = Post.objects.filter(Q(title__icontains = search_string) | Q(body__icontains = search_string)) #la búsqueda es en el título y en el cuerpo del post
    else :
        posts = Post.objects.all()       
    for post in posts:
        post.body = post.body[:200] + "..."
        
    #Chequea la página actual, si no se especifica, es la primera
    if not page_number: page_number = 1
    page_number = int(page_number)
    #Asigna a posts los posts de la página actual
    posts = posts[(page_number-1)*posts_per_page:page_number*posts_per_page] 
    page= {
        "current": page_number,
        "prev" : page_number-1,
        "next" : page_number+1,
    }   
        
    context = {'posts': posts, "user": user, 'profile_pic_form': profile_pic_form, 'search_form': search_form, "page": page}
        
    return render(request, 'home.html', context)

#API ------------------------------------------------

def search(request):
    search_form = SearchForm(request.POST)
    if search_form.is_valid():
        search_string = search_form.cleaned_data['search']
        return HttpResponseRedirect("/?search=" + search_string)
