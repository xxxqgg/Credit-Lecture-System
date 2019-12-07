from .models import Lecture
from rest_framework import serializers


class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = [
            'title',
            'lecture_time',
            'introduction',
            'capacity',
            'lecture_location',
            'lecturer',
            'lecturer_introduction'
        ]