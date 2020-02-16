from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import *
from .forms import LectureForm
from rest_framework import viewsets
from .serializers import LectureSerializer
from django.db import IntegrityError


# Create your views here.
class LectureViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Lecture.objects.all().order_by('-lecture_time')
    serializer_class = LectureSerializer


def index_view(request):
    lectures = Lecture.objects.order_by('lecture_time')
    context = {
        'lectures': lectures
    }
    return render(request, 'lecture_list.html', context)


def detail_view(request, id):
    lecture = get_object_or_404(Lecture, id=id)

    context = {
        'lecture': lecture
    }

    return render(request, 'lecture_detail.html', context)


def lecture_create_view(request):
    form = LectureForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = LectureForm()

    context = {
        'form': form
    }
    return render(request, 'lecture_create.html', context)


def lecture_signup_view(request, lecture_id):
    if request.user.is_anonymous:
        return redirect('login')
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    record = DrawResult()
    record.lecture = lecture
    record.student = request.user
    try:
        record.save()
    except IntegrityError:
        return redirect('lecture:index')

    return redirect('user:index')
