from django.conf import settings
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils import translation
from django.views.generic import ListView

from ..billing.models import Plan


def set_language(request):
    redirect_path = '/'
    response = HttpResponseRedirect(redirect_path)
    if request.method == 'POST':
        language = request.POST.get('language')
        if language:
            if language != settings.LANGUAGE_CODE and [
                lang for lang in settings.LANGUAGES if lang[0] == language
            ]:
                redirect_path = f'/{language}/'
        else:
            return response

        translation.activate(language)
        response = HttpResponseRedirect(redirect_path)
        response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)

    return response


class HomeView(ListView):
    template_name = 'main/home.html'
    context_object_name = 'plans'

    def get_queryset(self):
        return Plan.objects.all()


def get_started(request):
    template_name = 'main/get_started.html'
    context = {}
    return render(request, template_name, context)
