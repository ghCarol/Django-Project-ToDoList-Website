# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from models import Task
from serializers import TaskSerializer

import json

from rest_framework import viewsets

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics
from rest_framework import renderers
from rest_framework import reverse
from django.http import Http404


# 未用rest framework
@csrf_exempt
def to_do_list(request):
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


# 使用rest framework

class Tasklist(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    # def get(self, request, format=None):
    #     tasks = Task.objects.all()
    #     serializer = TaskSerializer(tasks, many=True)
    #     return Response(serializer.data)
    #
    # def post(self, request, format=None):
    #     serializer = TaskSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    读取, 更新 或 删除 一个task实例.
    """
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    # def get_object(self, id):
    #     try:
    #         return Task.objects.get(id=id)
    #     except Task.DoesNotExist:
    #         raise Http404
    #
    # def get(self, request, pk_id, format=None):
    #     task = self.get_object(pk_id)
    #     serializer = TaskSerializer(task)
    #     return Response(serializer.data)
    #
    # def put(self, request, pk_id, format=None):
    #     task = self.get_object(pk_id)
    #     serializer = TaskSerializer(task, data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def delete(self, request, pk_id, format=None):
    #     task = self.get_object(pk_id)
    #     task.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


# # API视图
# class TaskViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows groups to be viewed or edited.
#     """
#     queryset = Task.objects.all()
#     serializer_class = TaskSerializer

class TaskContent(generics.GenericAPIView):
    queryset = Task.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        task = self.get_object()
        return Response(task.content)
