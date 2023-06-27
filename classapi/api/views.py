from django.shortcuts import render
from rest_framework import viewsets
from api.models import classes, student
from api.serializers import classesserializers, studentserializer
from rest_framework.decorators import action
from rest_framework.response import Response

# Create your views here.

class classes(viewsets.ModelViewSet):
    queryset = classes.objects.all()
    serializer_class = classesserializers

    @action(detail=True, methods=['get'])
    def students_std(self, request, pk=None):
        class1 = classes.objects.get(pk=pk)
        std = student.objects.filter(class1=class1)
        std_serializer = studentserializer(std, many=True, context={'request': request})
        return Response(std_serializer.data)


class studentviewset(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = studentserializer

