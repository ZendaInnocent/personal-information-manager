from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('billing/', include('billing.urls')),
    path('todos/', include('todos.urls')),
    path('notes/', include('notes.urls')),
    path('accounts/', include('accounts.urls')),
    path('__debug__', include('debug_toolbar.urls')),
    path('tinymce/', include('tinymce.urls')),
]
