from django.shortcuts import render, get_object_or_404, redirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import LectureForm
from rest_framework import viewsets
from .serializers import LectureSerializer
from django.db import IntegrityError
from random import shuffle


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
        lecture = form.save()
        form = LectureForm()

    context = {
        'form': form
    }
    return render(request, 'lecture_create.html', context)


def lecture_signup_view(request, lecture_id):
    if request.user.is_anonymous:
        return redirect('user:login')
    lecture = get_object_or_404(Lecture, pk=lecture_id)
    if lecture.did_draw: # If a lecture is already drawn then we can not signup.
        return redirect('lecture:index')
    record = DrawResult()
    record.lecture = lecture
    record.student = request.user
    try:
        record.save()
    except IntegrityError:
        return redirect('lecture:index')

    return redirect('user:index')


def lecture_draw_view(request, lecture_id):
    if not request.user.is_staff:
        return redirect('lecture:index')
    success = draw(lecture_id)  # TODO: do different thing if fails to draw.
    return redirect('lecture:index')


def draw(lecture_id) -> bool:
    try:
        lecture = Lecture.objects.get(id=lecture_id)
    except ObjectDoesNotExist:
        return False
    if lecture.did_draw:
        return False
    results = DrawResult.objects.all().filter(lecture=lecture)
    # If the number of student signed up for the lecture is smaller than its capacity, all students can go.
    if len(results) <= lecture.capacity:
        for result in results:
            result.draw_status = DrawResult.Status.WIN
            result.save()

    # TODO: For now, all students have the same probability to get in the lecture.
    #  We need to implement the target class logic.
    else:
        results = list(results)
        shuffle(results)
        for i in range(lecture.capacity):
            results[i].draw_status = DrawResult.Status.WIN
            results[i].save()
        for i in range(lecture.capacity, len(results)):  # TODO: Fix efficiency here.
            results[i].draw_status = DrawResult.Status.MISSED
            results[i].save()
    lecture.did_draw = True
    lecture.save()
    return True
