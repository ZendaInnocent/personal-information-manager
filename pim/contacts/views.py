from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpRequest
from django.shortcuts import get_object_or_404, redirect, render
from django.template.response import TemplateResponse
from django.views.decorators.http import require_http_methods

from .forms import ContactForm
from .models import Contact


@login_required
def index(request) -> TemplateResponse:
    context = {'contacts': request.user.contacts.all()}
    return TemplateResponse(request, 'contacts/index.html', context)


@login_required
def contact_create_view(request):
    if request.method == 'POST':
        form = ContactForm(data=request.POST, initial={'user': request.user})

        if form.is_valid():
            form.save()
            messages.success(request, 'Contact created successful.')
            return redirect('contacts:index')
    else:
        form = ContactForm(initial={'user': request.user})

    context = {'form': form, 'title': 'Add'}
    return TemplateResponse(request, 'contacts/contact_form.html', context)


@login_required
def contact_detail_view(request, slug):
    contact = get_object_or_404(Contact, user=request.user, slug=slug)
    return render(request, 'contacts/contact_detail.html', {'contact': contact})


@login_required
def contact_update_view(request, slug):
    contact = get_object_or_404(Contact, user=request.user, slug=slug)

    if request.method == 'POST':
        form = ContactForm(instance=contact, data=request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'Contact updated successful.')
            return redirect('contacts:index')
    else:
        form = ContactForm(instance=contact)

    context = {'title': 'Edit', 'form': form, 'contact': contact}
    return render(request, 'contacts/contact_form.html', context)


@login_required
@require_http_methods(['POST'])
def contact_delete_view(request, slug):
    contact = get_object_or_404(Contact, user=request.user, slug=slug)
    contact.delete()
    messages.success(request, 'Contact deleted successful.')
    return redirect('contacts:index')


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
