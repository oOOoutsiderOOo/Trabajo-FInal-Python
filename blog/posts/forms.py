from django import forms

class NewPostForm(forms.Form):
    
    title = forms.CharField(label="Título", max_length=50)
    body = forms.CharField(label="Cuerpo", max_length=10000, widget=forms.Textarea)
    image = forms.ImageField(label="Imagen", required=False)

class EditPostForm(forms.Form):

    title = forms.CharField(label="Título", max_length=50)
    body = forms.CharField(label="Cuerpo", max_length=10000, widget=forms.Textarea)
    image = forms.ImageField(label="Imagen", required=False)
    
    #Se le pasa el id como input oculta para poder identificar el post a editar
    id = forms.IntegerField(widget=forms.HiddenInput())
    