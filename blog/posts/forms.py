from django import forms

class NewPostForm(forms.Form):
    title = forms.CharField(label="Title", max_length=50)
    body = forms.CharField(label="Body", max_length=10000, widget=forms.Textarea)