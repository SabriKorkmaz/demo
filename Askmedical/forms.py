from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Tag

class Search_Form(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = ''
        self.fields['q'].widget.attrs.update(
            {'class': 'form-control'})

#I created this form because in Django default form there was no email input
class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name', 'taglink']

