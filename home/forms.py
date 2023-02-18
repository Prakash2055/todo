from django import forms
from .models import *
from django.forms import ModelForm

class Task_form(forms.ModelForm):
    content= forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Add Task here'}))
    class Meta:
        model= Task
        # fields='__all__'
        fields=['content',]

class UpdateTaskForm(forms.ModelForm):
    class Meta:
        model= Task
        # fields='__all__'
        fields=['content','complete']

class todo_form(forms.ModelForm):
    task= forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder':'Add Task here'}))
    class Meta:
        model= todo
        fields=['task','user']


