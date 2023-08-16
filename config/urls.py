from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('', include('pim.main.urls')),
    path('admin/', admin.site.urls),
    path('billing/', include('pim.billing.urls')),
    path('todos/', include('pim.todos.urls')),
    path('notes/', include('pim.notes.urls')),
    path('accounts/', include('pim.accounts.urls')),
    path('__debug__', include('debug_toolbar.urls')),
    path('tinymce/', include('tinymce.urls')),
]
