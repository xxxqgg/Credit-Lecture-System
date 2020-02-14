from django.db import models
from django.urls import reverse
from user.models import LectureUser
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Lecture(models.Model):
    title = models.CharField(max_length=120)
    lecture_time = models.DateTimeField()
    introduction = models.TextField(blank=True, null=False)
    capacity = models.IntegerField()
    lecture_location = models.TextField()
    lecturer = models.TextField()
    lecturer_introduction = models.TextField()

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"id": self.id}) #f"/products/{self.id}/"

    def __str__(self):
        return self.title


class AttendanceLog(models.Model):

    lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE)
    student = models.OneToOneField(LectureUser, on_delete=models.CASCADE)
    didAttend = models.BooleanField('Attendance', default=False)

    def __str__(self):
        return self.lecture.title + ": " + self.student.username


class DrawResult(models.Model):
    id = models.IntegerField('id', primary_key=True)
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE,unique=False,primary_key=False)
    student = models.ForeignKey(LectureUser, on_delete=models.CASCADE,unique=False,primary_key=False)

    class Status(models.TextChoices):
        PENDING = 'PEN',_('Pending')
        WIN = 'WIN',_("Win")
        MISSED = 'MIS',_('Missed')
    draw_status = models.CharField(max_length=3, choices=Status.choices, default=Status.PENDING, null=False)
