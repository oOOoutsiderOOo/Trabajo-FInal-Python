from django.urls import path
from . import views

urlpatterns = [
    
    #Templates ----------------------------------------------------
    path('signup/', views.signupView, name='signupPage'),
    path('login/', views.loginView, name='loginPage'),
    
    #API ----------------------------------------------------------
    path('api/signup/', views.signup, name='signupQuery'),
    path("api/login/", views.login, name="loginQuery")
    
]