from django.forms import ModelForm, TextInput, Textarea, CheckboxInput
from .models import Task


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': TextInput(attrs={
                'class': 'w-full px-4 py-2 border text-gray-700  border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter task title',
            }),
            'description': Textarea(attrs={
                'class': 'w-full px-4 py-2 border text-gray-700  border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500',
                'placeholder': 'Enter task description',
                'rows': 5,
            }),
            'important': CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 focus:ring-blue-500 border-gray-300 rounded',
            }),
        }
