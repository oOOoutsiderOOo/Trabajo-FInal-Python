from django import forms 

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    password2 = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Confirme su contraseña', 'onkeyup' : 'validatePassword()'}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Nombre de usuario'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Contraseña'}))
    
class EditPicForm(forms.Form):
    profile_picture = forms.ImageField(label="Imagen de perfil", required=False)
    
