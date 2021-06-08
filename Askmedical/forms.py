from django import forms
from .models import Category

class Search_Form(forms.Form):
    q = forms.CharField()
    # c = forms.ModelChoiceField(
    #     queryset=Category.objects.all().order_by('name')
    # )