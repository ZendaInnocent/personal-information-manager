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
            ),
            'color': forms.TextInput(
                attrs={
                    'type': 'color',
                    'class': 'form-control form-control-color',
                },
            ),
        }
