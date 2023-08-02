from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from . import forms
from .models import Note


def index(request):
    notes = Note.objects.all()
    context = {'notes': notes}
    return render(request, 'notes/index.html', context)


class NoteCreateView(CreateView):
    model = Note
    form_class = forms.NoteForm


class NoteDetailView(DetailView):
    model = Note


class NoteUpdateView(UpdateView):
    model = Note
    form_class = forms.NoteForm


class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy('notes:notes-index')
