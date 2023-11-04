from django.contrib.auth.mixins import LoginRequiredMixin
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import ContactForm
from .models import Contact


def index(request):
    return TemplateResponse(request, 'contacts/index.html', {})


class ContactListView(LoginRequiredMixin, ListView):
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


contact_list = ContactListView.as_view()


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contacts:index')
    extra_context = {'title': 'Add'}

    def get_initial(self):
        return {'user': self.request.user}


contact_add = ContactCreateView.as_view()


class ContactDetailView(DetailView):
    model = Contact
    context_object_name = 'contact'


contact_detail = ContactDetailView.as_view()


class ContactUpdateView(UpdateView):
    model = Contact
    form_class = ContactForm
    extra_context = {'title': 'Edit'}


contact_edit = ContactUpdateView.as_view()
