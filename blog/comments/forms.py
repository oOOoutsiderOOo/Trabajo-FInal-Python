from django import forms

class NewCommentForm(forms.Form):
        
        content = forms.CharField(label="Contenido", max_length=1000, widget=forms.Textarea)
        user_id = forms.IntegerField(widget=forms.HiddenInput())
        post_id = forms.IntegerField(widget=forms.HiddenInput())
        response_to_id = forms.IntegerField(widget=forms.HiddenInput(), required=False)
        
class DeleteCommentForm(forms.Form):
    id = forms.IntegerField(widget=forms.HiddenInput())
    post_id = forms.IntegerField(widget=forms.HiddenInput())