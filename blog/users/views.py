from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import LoginForm, SignupForm
from .models import User

def signupView(request):
    form = SignupForm()
    return render(request, 'signup.html', {"form":form})

def loginView(request):
    form = LoginForm()
    token = request.COOKIES.get('access_token')
    if token:
        return HttpResponseRedirect("/")
    
    return render(request, 'login.html', {"form":form})

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

