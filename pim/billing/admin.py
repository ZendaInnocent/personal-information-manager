from django.contrib import admin

from pim.billing.models import Plan


@admin.register(Plan)
class PlanAdmin(admin.ModelAdmin):
    pass
