from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Todo, UserTodo
from .utils import get_order_value


@receiver(post_save, sender=Todo)
def create_user_todo(sender, created, instance, **kwargs):
    """Create a UserTodo when Todo is saved."""
    if created:
        UserTodo.objects.create(
            todo=instance, user=instance.user, order=get_order_value(user=instance.user)
        )
