# -*- coding: utf-8 -*-
from django.conf.urls import url

#from todo.views import *
#from .views import *

from . import views

from views import *

urlpatterns = [
    url(r'^$', TasksView.as_view(), name='tasks-list'),
    url(r'^clear/$', clear_resolved_tasks, name='tasks-clear'),
    url(r'^toggle/$', toggle_tasks, name='tasks-toggle'),

    url(r'^add/$', TaskCreateView.as_view(), name='task-create'),
    url(r'^toggle/(?P<task_id>\d+)/$', toggle_task, name='task-toggle'),
    url(r'^delete/(?P<pk>\d+)/$', TaskDeleteView.as_view(), name='task-delete'),
]
