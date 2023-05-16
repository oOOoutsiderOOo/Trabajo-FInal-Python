from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import ChangePasswordForm, LoginForm, SignupForm, EditPicForm, EditProfileForm
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

def profileView(request):
    uid = User.get_uid_from_token(request.COOKIES.get('access_token'))
    user = User.objects.get(id=uid)
    
    profile_pic_form = EditPicForm()
    change_password_form = ChangePasswordForm()
    
    context = {'user' : user, "profile_pic_form" : profile_pic_form, "change_password_form" : change_password_form}
    
    return render(request, 'profile.html', context)

def editProfileView(request):
    uid = User.get_uid_from_token(request.COOKIES.get('access_token'))
    user = User.objects.get(id=uid)
    profile_pic_form = EditPicForm()
    
    initial = {'name' : user.name, 'surname' : user.surname, 'email' : user.email, 'website': user.website}
    edit_form = EditProfileForm(initial=initial)
    
    context = {'user' : user, "profile_pic_form" : profile_pic_form, "edit_form" : edit_form}
    
    return render(request, 'edit_profile.html', context)

#API ----------------------------------------------------------

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            password2 = form.cleaned_data['password2']
            
            if password != password2:
                return HttpResponseRedirect("/signup/?error=pass_mismatch")
            
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
        form = LoginForm(request.POST)
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
    form = EditPicForm(request.POST, request.FILES)
    uid = User.get_uid_from_token(request.COOKIES.get('access_token'))
    user = User.objects.get(id=uid)
    if form.is_valid():
        user.profile_image = form.cleaned_data['profile_picture']
        user.save()
    return HttpResponseRedirect("/")

def editProfile(request):
    form = EditProfileForm(request.POST)
    uid = User.get_uid_from_token(request.COOKIES.get('access_token'))
    user = User.objects.get(id=uid)
    
    if form.is_valid():
        user.name = form.cleaned_data['name']
        user.surname = form.cleaned_data['surname']
        user.email = form.cleaned_data['email']
        user.website = form.cleaned_data['website']
        user.save()
    return HttpResponseRedirect("/profile/")

def changePassword(request):
    form = ChangePasswordForm(request.POST)
    
    uid = User.get_uid_from_token(request.COOKIES.get('access_token'))
    user = User.objects.get(id=uid)
    
    if form.is_valid():
        old_password = form.cleaned_data['old_password']
        new_password = form.cleaned_data['new_password']
        new_password2 = form.cleaned_data['new_password2']
        
        if old_password != user.password:
            return HttpResponseRedirect("/profile/?error=wrong_password")
        
        if new_password != new_password2:
            return HttpResponseRedirect("/profile/?error=pass_mismatch")
        
        user.password = new_password
        user.save()
        return HttpResponseRedirect("/profile/")
        


