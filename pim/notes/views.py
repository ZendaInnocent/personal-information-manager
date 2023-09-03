from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView

from . import forms
from .models import Note


@login_required
def index(request) -> HttpResponse:
    notes = Note.objects.filter(user=request.user)
    context = {'notes': notes}
    return render(request, 'notes/index.html', context)


class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    form_class = forms.NoteForm

    def get_initial(self):
        return {'user': self.request.user}


class NoteDetailView(UserPassesTestMixin, LoginRequiredMixin, DetailView):
    model = Note

    def test_func(self) -> bool:
        return self.get_object().user == self.request.user


class NoteUpdateView(UserPassesTestMixin, LoginRequiredMixin, UpdateView):
    model = Note
    form_class = forms.NoteForm

    def test_func(self) -> bool:
        return self.get_object().user == self.request.user


class NoteDeleteView(UserPassesTestMixin, LoginRequiredMixin, DeleteView):
    model = Note
    success_url = reverse_lazy('notes:notes-index')

    def test_func(self) -> bool:
        return self.get_object().user == self.request.user
