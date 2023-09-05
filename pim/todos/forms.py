from django import forms

from .models import Todo


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields: list | str = [
            'user',
            'text',
            'is_completed',
        ]
        widgets: dict[str, forms.TextInput] = {
            'user': forms.TextInput(attrs={'type': 'hidden'})
        }
