from django.db import models
from django.urls import reverse_lazy
from django.utils.text import slugify
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, blank=True, null=True)
    avatar = models.ImageField(upload_to='media/avatars', blank=True, null=True)
    is_favorite = models.BooleanField(default=False)
    email = models.EmailField(blank=True, null=True)
    phone_number = PhoneNumberField()

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy(
            'contacts:contact-detail',
            kwargs={'slug': self.slug},
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
