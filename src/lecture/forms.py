from django import forms
from .models import Lecture
from datetime import datetime


class LectureForm(forms.ModelForm):
    title = forms.CharField(label='Title',
                            )
    lecture_time = forms.DateTimeField(label='Time:', initial=datetime.now)

    introduction = forms.CharField(label='introduction')

    capacity = forms.IntegerField()

    lecture_location = forms.CharField()

    lecturer = forms.CharField()

    lecturer_introduction = forms.CharField()

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