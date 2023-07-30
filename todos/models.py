from django.db import models
from django.contrib.auth import get_user_model


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
    text = models.CharField(max_length=100)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

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
    order = models.PositiveSmallIntegerField()

    objects = UserTodoManager()

    class Meta:
        ordering = [
            'order',
        ]
