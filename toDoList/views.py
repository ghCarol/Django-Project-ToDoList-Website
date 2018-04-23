from django.shortcuts import render
from django.shortcuts import HttpResponse
from toDoList import models
# Create your views here.


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
