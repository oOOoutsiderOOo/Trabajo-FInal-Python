from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import LoginForm, SignupForm
from .models import User

#Views ----------------------------------------------------------

def signupView(request):
    form = SignupForm()
    return render(request, 'signup.html', {"form":form})

def loginView(request):
    form = LoginForm()
    token = request.COOKIES.get('access_token')
    if token:
        return HttpResponseRedirect("/")
    
    return render(request, 'login.html', {"form":form})

#TODO
def profileView(request):
    return render(request, 'profile.html', {})

#API ----------------------------------------------------------

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            role = "user"
            new_user = User(username=username, password=password, role=role)
            try:
                new_user.save()
            except:
                return HttpResponseRedirect("/signup/?error=username_taken")
            return HttpResponse("You have successfully signed up!")
 
# Chequea que el usuario exista y que la contraseña sea correcta. Si es así, setea la cookie user_id y redirige a home.       
def login(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return HttpResponse("Incorrect username or password. Please try again.")

            
            if user.password == password:
                response = HttpResponseRedirect("/")
                response.set_cookie('user_id', user.id, )
                return response
            else: 
                return HttpResponse("Incorrect username or password. Please try again.")
            

#Elimina las cookies user_id y access_token y redirige a login.
def logout(request):
    response = HttpResponseRedirect("/login/")
    response.delete_cookie('user_id')
    response.delete_cookie('access_token')
    return response

#Cambia la foto de perfil del usuario.
def editPic(request):
    uid = request.COOKIES.get('user_id')
    user = User.objects.get(id=uid)
    user.profile_image_url = request.POST.get('profile_picture')
    user.save()
    return HttpResponseRedirect("/")

