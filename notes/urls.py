from django.urls import path
from notes import views

urlpatterns = [
    path('notes/', views.NotesListView.as_view()),
    path('notes/<int:id>/', views.NotesDetailView.as_view()),
    path('notes/by_subject/', views.NotesBySubjectView.as_view()),
]