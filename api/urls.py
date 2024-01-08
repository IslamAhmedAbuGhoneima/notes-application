from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_routs, name='routs'),
    path('notes/', views.note_list, name='notes'),
    path('notes/<int:pk>/', views.get_note, name='note'),
]
