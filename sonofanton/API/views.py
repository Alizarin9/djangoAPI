from django.shortcuts import render
from rest_framework import viewsets

from .models import task_data, prompt_data, new_text_data, prompt_and_response_data
from .serializers import task_data_serializer, prompt_data_serializer, new_text_data_serializer, prompt_and_response_data_serializer


class task_data_view(viewsets.ModelViewSet):
    queryset = task_data.objects.all()
    serializer_class = task_data_serializer

class prompt_data_view(viewsets.ModelViewSet):
    queryset = prompt_data.objects.all()
    serializer_class = prompt_data_serializer

class new_text_data_view(viewsets.ModelViewSet):
    queryset = new_text_data.objects.all()
    serializer_class = new_text_data_serializer

class prompt_and_response_data_view(viewsets.ModelViewSet):
    queryset = prompt_and_response_data.objects.all()
    serializer_class = prompt_and_response_data_serializer