# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
import json
from models import Task
# from rest_framework import viewsets
# from serializers import TaskSerializer
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

# @csrf_exempt
# def index(request):
#     # request.POST
#     # request.GET
#     # return HttpResponse("Hello")
#     if request.method == "POST":
#         username = request.POST.get("username", None)
#         password = request.POST.get("password", None)
#         # temp = {"user": username, "pwd": password}
#         # user_list.append(temp)
#         models.UserInfo.objects.create(user=username, pwd=password)
#     user_list = models.UserInfo.objects.all()
#     return render(request, "index.html", {"data": user_list})

# 未用rest framework
@csrf_exempt
def toDoList(request):
    # 添加任务
    new_content = request.POST.get("new_content", None)
    if new_content is not None:
        task = Task.objects.create(content=new_content, finished=0)
        resp = {"id": task.id, "content": task.content, "finished": task.finished}
        return HttpResponse(json.dumps(resp), content_type="application/json")

    # 修改任务
    modified_id = request.POST.get("modified_id", None)
    modified_content = request.POST.get("modified_content", None)
    if modified_id is not None and modified_content is not None:
        task = Task.objects.get(id=modified_id)
        task.content = modified_content
        task.save()
        return HttpResponse()

    # 标记已完成的任务
    set_finished_task_id = request.POST.get("finished_id", None)
    if set_finished_task_id is not None:
        task = Task.objects.get(id=set_finished_task_id)
        task.finished = 1
        task.save()
        return HttpResponse()

    # 删除任务
    set_delete_id = request.POST.get("delete_id", None)
    if set_delete_id is not None:
        task = Task.objects.get(id=set_delete_id)
        task.delete()
        return HttpResponse()

    # 界面展示
    to_do_list = Task.objects.all()
    unfinished_tasks = []
    finished_tasks = []
    for task in to_do_list:
        if task.finished == 0:
            unfinished_tasks.append(task)
        elif task.finished == 1:
            finished_tasks.append(task)
    return render(request, "toDoList.html", {"unfinished_list": unfinished_tasks, "finished_list": finished_tasks})


# # 使用rest framework
# class TaskViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer
