# -*- coding: utf-8 -*-

from django.views.generic import ListView, CreateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from todo.models import Task
from todo.forms import TaskForm

TASK_LIST_URL = reverse_lazy('tasks-list')

# Tasks management

class TasksView(ListView):
    template_name="todo/tasks-list.html"
    model = Task

def clear_resolved_tasks(request):
    if request.method == 'POST':
        # Modify an object in POST only
        Task.objects.filter(is_resolved=True).delete()
    return HttpResponseRedirect(TASK_LIST_URL)

def toggle_tasks(request):
    if request.method == 'POST':
        # Modify an object in POST only
        try:
            task = Task.objects.all()[0]
        except IndexError:
            task = None
    
        if task is not None:
            status = not task.is_resolved
            Task.objects.all().update(is_resolved=status)

    return HttpResponseRedirect(TASK_LIST_URL)

# Task management

class TaskCreateView(CreateView):
    form_class = TaskForm
    
    success_url  = TASK_LIST_URL

    def form_invalid(self, form):
        return HttpResponseRedirect(self.success_url)

def toggle_task(request, task_id):
    if request.method == 'POST':
        # Modify an object in POST only
        task = get_object_or_404(Task, pk=task_id)
        
        task.is_resolved = not task.is_resolved
        task.save()

    return HttpResponseRedirect(TASK_LIST_URL)

class TaskDeleteView(DeleteView):
    model = Task
    success_url = TASK_LIST_URL
