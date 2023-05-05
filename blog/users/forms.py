from django import forms 

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    
class EditPicForm(forms.Form):
    profile_picture = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Pega la URL de tu imagen aquí'}))
