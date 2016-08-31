from django.utils import timezone

from django.shortcuts import render
from django.http import HttpResponse

from django.views.generic import TemplateView

from .forms import PostForm

# Create your views here.

from .models import Post

def allpostview(request):
    allpost = Post.objects.all().order_by('-published_date')
    context = {'allpost':allpost}
    return render(request, 'stairsblog/post_list.html',context)

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            post.published_date = timezone.now()
            post.save()
            allpost = Post.objects.all().order_by('-published_date')
            return render(request, 'stairsblog/post_list.html',{'allpost':allpost})
            
    else:
        form = PostForm()
    context={'form': form}
    return render(request, 'stairsblog/post_edit.html', context)




