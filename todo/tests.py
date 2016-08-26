# -*- coding: utf-8 -*-
"""
Todo : Tests
"""


from django.test import TestCase
from django.core.urlresolvers import reverse

from todo.models import Task


class TodoTest(TestCase):

    def setUp(self):
        task1 = Task.objects.create(content=u'Ma première tâche', is_resolved=True)
        task2 = Task.objects.create(content=u'Ma seconde tâche', is_resolved=False)
        task3 = Task.objects.create(content=u'Ma troisième tâche', is_resolved=True)
        task4 = Task.objects.create(content=u'Ma quatrième tâche', is_resolved=False)


    def test_task_list(self):
        url = reverse('tasks-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.context['object_list']), Task.objects.count())


    def test_tasks_clear(self):
        url = reverse('tasks-clear')

        nb_tasks = Task.objects.count()
        response = self.client.post(url)
        self.assertEqual(nb_tasks-2, Task.objects.count())


    def test_tasks_toggle(self):
        url = reverse('tasks-toggle')

        nb_tasks = Task.objects.filter(is_resolved=True).count()
        response = self.client.post(url)
        self.assertEqual(0, Task.objects.filter(is_resolved=True).count())

        response = self.client.post(url)
        self.assertEqual(nb_tasks+2, Task.objects.filter(is_resolved=True).count())


    def test_task_creation(self):
        url = reverse('task-create')

        nb_tasks = Task.objects.count()
        response = self.client.post(url, {'content': u'Ma cinquième tâche'})
        self.assertEqual(nb_tasks+1, Task.objects.count())


    def test_task_toggle(self):
        task_id = Task.objects.all()[0].id
        url = reverse('task-toggle', args=[task_id])

        status = Task.objects.get(pk=task_id).is_resolved
        response = self.client.post(url)
        self.assertEqual(status, not Task.objects.get(pk=task_id).is_resolved)


    def test_task_delete(self):
        task_id = Task.objects.all()[0].id
        url = reverse('task-delete', args=[task_id])

        nb_tasks = Task.objects.count()
        response = self.client.post(url)
        self.assertEqual(nb_tasks-1, Task.objects.count())

        response = self.client.post(url)
        self.assertEqual(response.status_code, 404)
