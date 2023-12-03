from django.urls import path
from . import views
urlpatterns = [
    path('', views.get_routs, name='routs'),
    path('notes/', views.note_list, name='notes'),
    path('notes/<int:pk>/', views.get_note, name='note'),
    # path('notes/create/', views.create_note, name='create'),
    # path('notes/<int:pk>/update/', views.update_note, name='update'),
    # path('notes/<int:pk>/delete/', views.delete_note, name='delete'),
]
