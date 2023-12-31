from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse_lazy
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name='contacts',
    )
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(_('name'), max_length=100)
    title = models.CharField(_('title'), max_length=100, blank=True, null=True)
    avatar = models.ImageField(
        _('avatar'),
        upload_to='avatars',
        blank=True,
        null=True,
        default='avatars/User Avatar.jpg',
    )
    is_favorite = models.BooleanField(_('is favorite'), default=False)
    email = models.EmailField(_('email'), blank=True, null=True)
    phone_number = PhoneNumberField(_('phone number'))
    organization = models.CharField(
        _('organization'), max_length=100, blank=True, null=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy(
            'contacts:contact-detail',
            kwargs={'slug': self.slug},
        )

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name) + '-' + get_random_string(8)
        return super().save(*args, **kwargs)

    def toggle_favorite(self):
        self.is_favorite = not self.is_favorite
        self.save()
