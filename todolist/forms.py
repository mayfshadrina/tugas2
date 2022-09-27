from django import forms
from todolist.models import Task

class create_form(forms.Form):
    title = forms.CharField(label = "Title")
    description = forms.CharField(label = "Description")