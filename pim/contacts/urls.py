from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.contact_add, name='contact-add'),
    path('<slug:slug>/', views.contact_detail, name='contact-detail'),
]
