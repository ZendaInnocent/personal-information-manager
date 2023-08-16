from django.contrib.auth import get_user_model
from django.db import models

from billing.models import Plan

User = get_user_model()


class Subscription(models.Model):
    class STATES:
        ACTIVE = 'active'
        INACTIVE = 'inactive'
        CANCELED = 'canceled'
        ENDED = 'ended'

    STATE_CHOICES = (
        (STATES.ACTIVE, 'Active'),
        (STATES.INACTIVE, 'Inactive'),
        (STATES.CANCELED, 'Canceled'),
        (STATES.ENDED, 'Ended'),
    )

    plan = models.ForeignKey(
        Plan, models.CASCADE, help_text='The plan the user is subscribed to.'
    )
    description = models.CharField(max_length=1024, blank=True, null=True)
    user = models.ForeignKey(
        User,
        related_name='subscriptions',
        on_delete=models.CASCADE,
        help_text='The user who is subscribed to the plan.',
    )
    trial_end = models.DateField(
        blank=True,
        null=True,
        help_text='The date at which the trial ends. \
            If set, overrides the computed trial end date from the plan.',
    )
    start_date = models.DateField(
        blank=True, null=True, help_text='The starting date for the subscription.'
    )
    cancel_date = models.DateField(
        blank=True, null=True, help_text='The date when the subscription was canceled.'
    )
    ended_at = models.DateField(
        blank=True, null=True, help_text='The date when the subscription ended.'
    )
    state = models.CharField(
        max_length=12,
        choices=STATE_CHOICES,
        default=STATES.INACTIVE,
        help_text='The state the subscription is in.',
    )

    def clean(self):
        errors = dict()

        if self.state not in [self.STATES.CANCELED, self.STATES.ENDED]:
            errors.update(
                {
                    'ended_at': 'The ended at date cannot be set if \
                        the subscription is not canceled or ended.',
                }
            )
