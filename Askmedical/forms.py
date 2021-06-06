from django import forms

class Search_Form(forms.Form):
    q = forms.CharField()