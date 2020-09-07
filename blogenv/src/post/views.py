from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Post
from .forms import PostForm
# Create your views here.
def list_post(request):
    posts=Post.objects.all();
    context={'posts':posts}
    return render(request,"post/list_post.html",context)

def detail_post(request,post_id):
    post=Post.objects.get(id=post_id)
    context={'post':post}
    return render(request,"post/detail_post.html",context)

def create_post(request):
    form=PostForm()
    if(request.method=="POST"):
       form=PostForm(request.POST)
       if form.is_valid():
            form.save()
            print("post has been saved")
            return HttpResponseRedirect("/posts")
    context={'form':form}
    return render(request,"post/create_post.html",context)
def update_post(request,post_id):
    post=Post.objects.get(id=post_id)
    form=PostForm(request.POST or None,instance=post)
    if form.is_valid():
       form.save()
       print("post updated with id {}".format(post_id))
       return HttpResponseRedirect("/posts")
    context={'form':form}
    return render(request,"post/create_post.html",context)

def delete_post(request,post_id):
    post=Post.objects.get(id=post_id)
    if post is not None:
       print("post deleted with id {}".format(post_id))
       post.delete()
    return HttpResponseRedirect("/posts")