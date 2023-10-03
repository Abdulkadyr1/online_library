from django import forms


class Library(forms.Form):
    name = forms.CharField(max_length=20, min_length=2)
    Author = forms.CharField(max_length=20, min_length=4)
