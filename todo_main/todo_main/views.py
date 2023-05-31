from django.shortcuts import render
from todo.models import Task


def home(request):
    tasks = Task.objects.filter(is_completed=False).order_by('updated_at')
    completed_tasks = Task.objects.filter(is_completed=True).order_by('updated_at')
    context = {
        'tasks1':tasks,
        'completed_tasks1':completed_tasks,
    }
    return render(request, 'home-todo.html',context)
