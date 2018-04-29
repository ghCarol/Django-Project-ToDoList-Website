# -*- coding: UTF-8 -*-
from django.conf.urls import url, include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from toDoList import views
from rest_framework.authtoken import views as drf_views

# router = routers.DefaultRouter()
# router.register(r'tasks', views.TaskViewSet)
# router.include_format_suffixes = False

urlpatterns = [
    # url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),  # rest-framework使用可浏览的API
    url(r'^tasks/$', views.Tasklist.as_view()),
    url(r'^tasks/(?P<pk>[0-9]+)/$', views.TaskDetail.as_view()),
    url(r'^auth$', drf_views.obtain_auth_token, name='auth'),

]

urlpatterns = format_suffix_patterns(urlpatterns)
