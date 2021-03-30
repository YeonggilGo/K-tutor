from rest_framework import serializers
from .models import *

class ExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExamResult
        field = '__all__'


class ExamSerializer(serializers.Serializer):
    problem = serializers.DictField()
    cs = serializers.CharField(max_length=100)
