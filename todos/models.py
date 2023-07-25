from django.db import models

class Todo(models.Model):
    text = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = [
            '-created_at',
        ]

    def __str__(self):
        return self.text
    
