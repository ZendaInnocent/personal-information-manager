from django import forms

from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'user',
            'name',
            'phone_number',
            'title',
            'avatar',
            'is_favorite',
            'email',
        ]
        widgets = {
            'user': forms.TextInput(
                attrs={'type': 'hidden'},
            ),
        }
