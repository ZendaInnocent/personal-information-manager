from typing import Any

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q
from django.http import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views import generic

from .forms import ContactForm
from .models import Contact


@login_required
def index(request) -> TemplateResponse:
    return TemplateResponse(request, 'contacts/index.html', {})


class ContactListView(LoginRequiredMixin, generic.ListView):
    context_object_name = 'contacts'

    def get_queryset(self):
        return self.request.user.contacts.all()


contact_list = ContactListView.as_view()


class ContactCreateView(LoginRequiredMixin, generic.CreateView):
    model = Contact
    form_class = ContactForm
    extra_context = {'title': 'Add'}

    def get_initial(self):
        return {'user': self.request.user}

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        response = super().dispatch(request, *args, **kwargs)
        response['HX-Trigger'] = 'loadcontacts'
        return response


contact_add = ContactCreateView.as_view()


class ContactDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
    model = Contact
    context_object_name = 'contact'

    def test_func(self) -> bool | None:
        return self.get_object().user == self.request.user

    def dispatch(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        response = super().dispatch(request, *args, **kwargs)
        response['HX-Trigger'] = 'loadcontacts'
        return response


contact_detail = ContactDetailView.as_view()


class ContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, generic.UpdateView):
    model = Contact
    form_class = ContactForm
    extra_context = {'title': 'Edit'}

    def test_func(self) -> bool | None:
        return self.get_object().user == self.request.user


contact_edit = ContactUpdateView.as_view()


class ContactDeleteView(LoginRequiredMixin, UserPassesTestMixin, generic.DeleteView):
    model = Contact
    success_url = reverse_lazy('contacts:index')

    def test_func(self) -> bool | None:
        return self.get_object().user == self.request.user


contact_delete = ContactDeleteView.as_view()


@login_required
def contact_search(request: HttpRequest) -> TemplateResponse:
    q = request.GET.get('q', None)
    contacts = []
    if q is not None:
        contacts = request.user.contacts.filter(
            Q(name__icontains=q) | Q(title__icontains=q) | Q(organization__icontains=q)
        )

    return TemplateResponse(
        request, 'contacts/contact_list.html', {'contacts': contacts}
    )


@login_required
def toggle_favorite(request: HttpRequest, slug: str) -> TemplateResponse:
    contact: Contact = get_object_or_404(Contact, slug=slug, user=request.user)
    contact.toggle_favorite()
    context = {'contact': contact}
    response = TemplateResponse(request, 'contacts/favorite.html', context)
    response['HX-Trigger'] = 'loadcontacts'
    return response
