from .models import Lecture
from rest_framework import serializers


class LectureSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Lecture
        fields = [
            'id',
            'title',
            'lecture_time',
            'draw_date',
            'introduction',
            'capacity',
            'lecture_location',
            'lecturer',
            'lecturer_introduction',
            'target_class',
            'did_draw',
        ]
