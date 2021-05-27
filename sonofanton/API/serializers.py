from rest_framework import serializers
from .models import task_data, prompt_data, new_text_data, prompt_and_response_data

class task_data_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = task_data
        fields = '__all__'

class prompt_data_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = prompt_data
        fields = '__all__'

class new_text_data_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = new_text_data
        fields = '__all__'

class prompt_and_response_data_serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = prompt_and_response_data
        fields = '__all__'