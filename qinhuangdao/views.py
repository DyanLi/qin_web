from django.shortcuts import render
from django.http import HttpResponse
from qinhuangdao.models import Qinhuangdao
from datetime import datetime

def index(request):
    return render(request, "index.html")

def detail(request,my_args):
    # my_args = page now

    # if not my_args:
    #     my_args = 1
    # print(type(my_args))

    try:
        my_args = int(my_args)
    except:
        my_args = 1

    if my_args < 1:
        my_args = 1

    start = 1
    end  = Qinhuangdao.objects.all().__len__()

    if my_args == start :
        before_page = 1
    else:
        before_page = my_args - 1

    if my_args > end-1:
        next_page = my_args
    else:
        next_page = my_args +1

    post = Qinhuangdao.objects.all()[my_args-1]
    # str = ("datetime = %s, d1 = %s, v1 = %s"
    #     % (post.datetime, post.direction1, post.velocity1))
    # return HttpResponse(str)
    return render(request, "detail.html", {'post': post,'current_page':my_args,'before_page':before_page,'next_page':next_page,'end_page':end})

def draw(request,my_args):
    # post = Qinhuangdao.objects.all()[int(my_args)]
    # return render(request, "draw.html", {'post': post})
    try:
        my_args = int(my_args)
    except:
        my_args = 1

    if my_args < 1:
        my_args = 1

    start = 1
    end  = Qinhuangdao.objects.all().__len__()

    if my_args == start :
        before_page = 1
    else:
        before_page = my_args - 1

    if my_args > end-1:
        next_page = my_args
    else:
        next_page = my_args +1

    post = Qinhuangdao.objects.all()[my_args-1]
    # str = ("datetime = %s, d1 = %s, v1 = %s"
    #     % (post.datetime, post.direction1, post.velocity1))
    # return HttpResponse(str)
    return render(request, "draw.html", {'post': post,'current_page':my_args,'before_page':before_page,'next_page':next_page,'end_page':end})


def show(request):
    post = Qinhuangdao.objects.all()
    return render(request, "show.html", {'post':post})

