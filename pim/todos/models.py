from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class TodoManager(models.Manager):
    def prefetched_user(self):
        return self.get_queryset().select_related('user')


class Todo(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="todos",
    )
    text = models.CharField(_('text'), max_length=100)
    is_completed = models.BooleanField(_('is_completed'), default=False)
    created_at = models.DateTimeField(_('created_at'), auto_now_add=True)
    updated_at = models.DateTimeField(_('updated_at'), auto_now=True)

    objects = TodoManager()

    class Meta:
        ordering = [
            "-created_at",
        ]

    def __str__(self):
        return self.text


class UserTodoManager(models.Manager):
    def prefetched_user_todo(self):
        return self.get_queryset().prefetch_related('user', 'todo')


class UserTodo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    todo = models.ForeignKey(Todo, on_delete=models.CASCADE)
    order = models.PositiveSmallIntegerField(_('order'))

    objects = UserTodoManager()

    class Meta:
        ordering = [
            'order',
        ]
