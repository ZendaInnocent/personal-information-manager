from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse
from tinymce import models as tinymce_models

User = get_user_model()


class Note(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='notes',
    )
    title = models.CharField(max_length=100)
    content = tinymce_models.HTMLField()
    color = models.CharField(max_length=7, default='#FFFFFF')

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            '-modified_at',
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('notes:note-detail', kwargs={'pk': self.pk})
