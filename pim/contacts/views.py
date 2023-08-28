from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

from .models import Contact


def index(request):
    template_name = 'contacts/index.html'
    context = {'contacts': Contact.objects.all()}
    return render(request, template_name, context)


class ContactCreateView(CreateView):
    model = Contact
    fields = [
        'name',
        'phone_number',
        'title',
        'avatar',
        'is_favorite',
        'email',
    ]
    success_url = reverse_lazy('contacts:index')


contact_add = ContactCreateView.as_view()


class ContactDetailView(DetailView):
    model = Contact
    context_object_name = 'contact'


contact_detail = ContactDetailView.as_view()
