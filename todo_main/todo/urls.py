from django.urls import path,include
from.import views

urlpatterns = [
    # Add Tasks
    path('addTask/',views.addTask,name = 'addTask'),
    # Mark as done
    path('mark_as_done/<int:pk>/',views.mark_as_done,name = 'mark_as_done'),
    # Undo
    path('undo_task/<int:pk>/',views.undo_task,name = 'undo_task'),
    # Edit
    path('edit_task/<int:pk>/',views.edit_task,name='edit_task'),
    # Delete
    path('delete_task/<int:pk>/',views.delete_task,name='delete_task'),
]
