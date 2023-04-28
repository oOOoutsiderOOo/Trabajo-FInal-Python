from django import forms 

class SignupForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))

class LoginForm(forms.Form):
    username = forms.CharField(max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(max_length=50, widget=forms.PasswordInput(attrs={'placeholder': 'Password'}))
    
class EditPicForm(forms.Form):
    profile_picture = forms.CharField(max_length=500, widget=forms.TextInput(attrs={'placeholder': 'Paste your image URL here'}))
