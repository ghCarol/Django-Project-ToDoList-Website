from rest_framework import serializers
from toDoList import models


class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = models.Task
        fields = ('id', 'content', 'finished')
