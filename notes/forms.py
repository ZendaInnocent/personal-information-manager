from django import forms

from .models import Note


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = (
            'user',
            'title',
            'content',
            'color',
        )
        widgets = {
            'user': forms.TextInput(
                attrs={
                    'type': 'hidden',
                }
            )
        }
