from django.urls import path
from . import views

urlpatterns = [
    
    #Templates ----------------------------------------------------
    path('signup/', views.signupView, name='signupPage'),
    path('login/', views.loginView, name='loginPage'),
    path('profile/', views.profileView, name='profilePage'),
    path('profile/edit/', views.editProfileView, name='editProfileView'),
    
    #API ----------------------------------------------------------
    path('api/signup/', views.signup, name='signupQuery'),
    path("api/login/", views.login, name="loginQuery"),
    path("api/logout/", views.logout, name="logoutQuery"),
    path("api/update_pic/", views.editPic, name="updatePicQuery"),
    path("api/edit_profile/", views.editProfile, name="editProfileQuery"),
    path("api/change_password/", views.changePassword, name="changePasswordQuery")
    
    
]