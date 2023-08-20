from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.urls import include, path

urlpatterns = i18n_patterns(
    path('', include('pim.main.urls')),
    path('admin/', admin.site.urls),
    path('billing/', include('pim.billing.urls')),
    path('todos/', include('pim.todos.urls')),
    path('notes/', include('pim.notes.urls')),
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('pim.accounts.urls')),
    path('__debug__', include('debug_toolbar.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('rosetta/', include('rosetta.urls')),
    prefix_default_language=False,
)
