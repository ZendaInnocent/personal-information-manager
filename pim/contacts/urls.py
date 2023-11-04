from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.contact_add, name='contact-add'),
    path('search/', views.contact_search, name='contact-search'),
    path('list/', views.contact_list, name='contact-list'),
    path('<slug:slug>/', views.contact_detail, name='contact-detail'),
    path('<slug:slug>/edit/', views.contact_edit, name='contact-edit'),
    path('<slug:slug>/delete/', views.contact_delete, name='contact-delete'),
]
