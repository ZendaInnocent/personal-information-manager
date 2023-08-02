from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='notes-index'),
    path('create/', views.NoteCreateView.as_view(), name='note-create'),
    path('<slug:slug>/', views.NoteDetailView.as_view(), name='note-detail'),
    path(
        '<slug:slug>/update/',
        views.NoteUpdateView.as_view(),
        name='note-update',
    ),
    path(
        '<slug:slug>/delete/',
        views.NoteDeleteView.as_view(),
        name='note-delete',
    ),
]
