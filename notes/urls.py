from django.urls import path

from . import views

app_name = 'notes'

urlpatterns = [
    path('', views.index, name='notes-index'),
    path('create/', views.NoteCreateView.as_view(), name='note-create'),
]
