from django.urls import path

from . import views

app_name = 'contacts'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.contact_create_view, name='contact-create'),
    path('search/', views.contact_search_view, name='contact-search'),
    path('<slug:slug>/', views.contact_detail_view, name='contact-detail'),
    path('<slug:slug>/edit/', views.contact_update_view, name='contact-edit'),
    path('<slug:slug>/delete/', views.contact_delete_view, name='contact-delete'),
    path(
        '<slug:slug>/toggle-favorite/',
        views.toggle_favorite,
        name='contact-toggle-favorite',
    ),
]
