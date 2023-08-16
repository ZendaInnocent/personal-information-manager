from django.core.validators import MinValueValidator
from django.db import models

from billing.utils import INTERVALS as DATE_INTERVALS
from billing.utils import currencies


class IntervalChoices(models.TextChoices):
    DAY = DATE_INTERVALS.DAY, 'Day'
    WEEK = DATE_INTERVALS.WEEK, 'Week'
    MONTH = DATE_INTERVALS.MONTH, 'Month'
    YEAR = DATE_INTERVALS.YEAR, 'Year'


class Plan(models.Model):
    INTERVALS = IntervalChoices

    name = models.CharField(
        max_length=100,
        help_text='Display name of the plan.',
    )
    interval = models.CharField(
        choices=INTERVALS.choices,
        max_length=12,
        default=INTERVALS.MONTH,
        help_text='The frequency with which a subscription should be billed.',
    )
    interval_count = models.PositiveIntegerField(
        help_text='The number of intervals between eac subscription billing.'
    )
    amount = models.DecimalField(
        max_digits=19,
        decimal_places=2,
        validators=[MinValueValidator(0.0)],
        help_text=(
            'The amount in the specified currency to be charged \
                on the interval specified.'
        ),
    )
    currency = models.CharField(
        choices=currencies,
        max_length=5,
        default='TZS',
        help_text='The currency on which the subscription will be charged.',
    )
    trial_period_days = models.PositiveIntegerField(
        null=True,
        blank=True,
        help_text=(
            'Number of trial period days granted when \
            subscribing a customer to this plan.'
        ),
        verbose_name='Trial days',
    )
    prebill_plan = models.BooleanField(
        null=True,
        help_text=(
            'If this is  set to True, then the plan base \
                amount will be billed at the beginning of the \
                    billing cycle rather than after the end.'
        ),
    )
    enabled = models.BooleanField(
        default=True, help_text='Whether to accept subscription.'
    )

    class Meta:
        ordering = (
            'amount',
            'name',
        )

    def __str__(self):
        return self.name
