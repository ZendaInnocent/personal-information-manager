from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = [
            'user',
            'text',
            'is_completed',
        ]
        widgets = {
            'user': forms.HiddenInput(),
        }
