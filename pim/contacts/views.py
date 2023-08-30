from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import ContactForm
from .models import Contact


class ContactListView(LoginRequiredMixin, ListView):
    context_object_name = 'contacts'

    def get_queryset(self):
        return Contact.objects.filter(user=self.request.user)


index = ContactListView.as_view()


class ContactCreateView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = reverse_lazy('contacts:index')

    def get_initial(self):
        return {'user': self.request.user}


contact_add = ContactCreateView.as_view()


class ContactDetailView(DetailView):
    model = Contact
    context_object_name = 'contact'


contact_detail = ContactDetailView.as_view()
