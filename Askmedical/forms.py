from django import forms
from .models import Category

class Search_Form(forms.Form):
    q = forms.CharField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['q'].label = ''
        self.fields['q'].widget.attrs.update(
            {'class': 'form-control'})
