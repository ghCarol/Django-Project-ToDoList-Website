# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
from toDoList import models
from models import ToDoListModel
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def index(request):
    # request.POST
    # request.GET
    # return HttpResponse("Hello")
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # temp = {"user": username, "pwd": password}
        # user_list.append(temp)
        models.UserInfo.objects.create(user=username, pwd=password)
    user_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data": user_list})


@csrf_exempt
def toDoList(request):
    # request.POST
    # request.GET

    new_content = request.POST.get("new_content", None)
    if new_content is not None:
        task = ToDoListModel.objects.create(content=new_content, finished=0)  # todo controller收到传值
        resp = {"id": task.id, "content": task.content, "finished": task.finished}
        return HttpResponse(json.dumps(resp), content_type="application/json")
    to_do_list = ToDoListModel.objects.all()
    unfinished_tasks = []
    finished_tasks = []
    for task in to_do_list:
        if task.finished == 0:
            unfinished_tasks.append(task)
        elif task.finished == 1:
            finished_tasks.append(task)
    return render(request, "toDoList.html", {"unfinished_list": unfinished_tasks, "finished_list": finished_tasks})


