from .models import LectureUser, Class
from rest_framework import serializers


class ClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Class
        fields = [
            'major',
            'grade',
            'class_number'
        ]
