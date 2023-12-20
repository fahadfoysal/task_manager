from django import forms
from .models import Task, TaskImage

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description',
                  'due_date', 'priority', 'is_completed']
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'datetime-local'})
        }

class TaskImageForm(forms.ModelForm):
    class Meta:
        model = TaskImage
        fields = ['image']