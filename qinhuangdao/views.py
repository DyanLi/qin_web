from django.shortcuts import render
from django.http import HttpResponse
from qinhuangdao.models import Qinhuangdao
from datetime import datetime

def index(request):
    post = Qinhuangdao.objects.all()[1]
    return render(request, "show.html", {'post': post})

def detail(request,my_args):
    post = Qinhuangdao.objects.all()[int(my_args)]
    str = ("datetime = %s, d1 = %s, v1 = %s"
        % (post.datetime, post.direction1, post.velocity1))
    return HttpResponse(str)
