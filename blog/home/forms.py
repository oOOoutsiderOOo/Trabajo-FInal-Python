from django import forms

class SearchForm(forms.Form):
    search = forms.CharField(label="Buscar", max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Buscar'}))