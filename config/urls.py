from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from pim.main import views as main_views

urlpatterns = [
    path('set-language/', main_views.set_language, name='set-language'),
    path('__debug__', include('debug_toolbar.urls')),
    path('__reload__/', include('django_browser_reload.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('rosetta/', include('rosetta.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('pim.main.urls')),
    path('appointments/', include('pim.appointments.urls')),
    path('contacts/', include('pim.contacts.urls')),
    path('admin/', admin.site.urls),
    path('billing/', include('pim.billing.urls')),
    path('todos/', include('pim.todos.urls')),
    path('notes/', include('pim.notes.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('pim.accounts.urls')),
    prefix_default_language=False,
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
