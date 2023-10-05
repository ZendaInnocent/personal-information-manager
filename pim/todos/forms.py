from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            'user',
            'text',
            'due_date',
            'is_completed',
        ]
        widgets = {
            'user': forms.HiddenInput(),
            'due_date': forms.DateTimeInput(attrs={'type': 'date'}),
        }
