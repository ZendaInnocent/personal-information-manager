from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='media/avatars')
    is_favorite = models.BooleanField(default=False)
    email = models.EmailField()
    phone = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
