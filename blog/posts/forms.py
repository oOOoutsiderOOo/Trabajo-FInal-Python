from django import forms

class NewPostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    body = forms.CharField(label="Body", max_length=10000, widget=forms.Textarea)

class EditPostForm(forms.Form):
    
    def __init__(self,   *args, **kwargs):
        super().__init__(*args, **kwargs)

    title = forms.CharField(label="Title", max_length=50)
    body = forms.CharField(label="Body", max_length=10000, widget=forms.Textarea)
    id = forms.IntegerField(widget=forms.HiddenInput())
    