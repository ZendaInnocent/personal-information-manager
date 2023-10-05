from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

from .utils import get_order_value

User = get_user_model()


class Todo(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="todos",
    )
    text = models.CharField(_('text'), max_length=100)
    is_completed = models.BooleanField(_('is completed'), default=False)
    order = models.PositiveIntegerField()
    due_date = models.DateTimeField(blank=True, null=True)

    created_at = models.DateTimeField(
        _('created_at'),
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    class Meta:
        ordering: list[str] = [
            'order',
        ]

    def __str__(self) -> str:
        return self.text

    def save(self, *args, **kwargs):
        if self.order is None:
            self.order = get_order_value(self.user)
        return super().save(*args, **kwargs)

    def toggle_completed(self) -> None:
        self.is_completed: bool = not self.is_completed
        self.save()
