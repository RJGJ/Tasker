from django.forms import ModelForm, TextInput, EmailInput, DateInput, fields
from .models import *
from django.db.models.query_utils import DeferredAttribute


class UserForm(ModelForm):
    class Meta:
        model = User
        widgets = {

            'first_name': TextInput(attrs={
                'placeholder': model.first_name if not type(model.first_name) == DeferredAttribute else ''
            }),

            'last_name': TextInput(attrs={
                'placeholder': model.last_name if not type(model.last_name) == DeferredAttribute else ''
            }),

            'username': TextInput(attrs={
                'placeholder': model.username,
            }),

            'email': EmailInput(attrs={
                'placeholder': model.email,
            }),

        }
        fields = [
            'image',
            'first_name',
            'last_name',
            'username',
            'email'
        ]


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            'name',
            'description',
            'due_on',
            'assignee',
        ]
        widgets = {
            'due_on': DateInput(attrs={'type': 'date'})
        }
        labels = {
            'due_on': ('Target Date:'),
        }


class DepartmentFileForm(ModelForm):
    class Meta:
        model = DepartmentFile
        exclude = ['uploader', 'department']
