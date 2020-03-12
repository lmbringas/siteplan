from django.shortcuts import render, get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from .models import Task, WBS
from .serializers import TaskSerializer, WBSSerializer


class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def list(self, request):
        queryset = Task.objects.filter(parent__exact=None,)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Task.objects.all()
        task = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)


class WBSViewSet(viewsets.ModelViewSet):
    queryset = WBS.objects.all()
    serializer_class = WBSSerializer
