from django.shortcuts import render
from django.views.generic import ListView

from pim.billing.models.plans import Plan


class HomeView(ListView):
    template_name = 'main/home.html'
    context_object_name = 'plans'

    def get_queryset(self):
        return Plan.objects.all()


def get_started(request):
    template_name = 'main/get_started.html'
    context = {}
    return render(request, template_name, context)
