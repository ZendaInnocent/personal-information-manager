from django.urls import include, path

app_name = 'accounts'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
]
