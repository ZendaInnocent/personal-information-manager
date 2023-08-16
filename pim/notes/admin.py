from django.contrib import admin

from .models import Note


@admin.register(Note)
class NoteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'title',
        'content',
        'color',
    )
    list_display_links = (
        'id',
        'title',
        'content',
    )
