from django.shortcuts import render
from django.http import HttpResponse
from qinhuangdao.models import Qinhuangdao
from datetime import datetime

def index(request):
    return render(request, "index.html")

def detail(request,my_args):
    post = Qinhuangdao.objects.all()[int(my_args)]
    # str = ("datetime = %s, d1 = %s, v1 = %s"
    #     % (post.datetime, post.direction1, post.velocity1))
    # return HttpResponse(str)
    return render(request, "detail.html", {'post': post})

def draw(request,my_args):
    post = Qinhuangdao.objects.all()[int(my_args)]
    return render(request, "draw.html", {'post': post})

def show(request):
    post = Qinhuangdao.objects.all()
    return render(request, "show.html", {'post':post})

