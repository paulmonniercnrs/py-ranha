"""pyranha_apps URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
<<<<<<< HEAD
from django.conf.urls import url , include
=======

from django.conf.urls import url, include

>>>>>>> f23ae85befe02d3777ba15f148cf215727696739
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
<<<<<<< HEAD
    url(r'^todo_app/', include('todo.urls')),
=======
    url(r'^todo_app/', include('todo.urls'))
>>>>>>> f23ae85befe02d3777ba15f148cf215727696739
]
