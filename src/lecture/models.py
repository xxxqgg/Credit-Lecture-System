from django.db import models
from django.urls import reverse
from django.conf import settings
from user.models import Class
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Lecture(models.Model):
    title = models.CharField(max_length=120)
    lecture_time = models.DateTimeField()
    draw_date = models.DateField(blank=False, null=False)
    introduction = models.TextField(blank=True, null=False)
    capacity = models.IntegerField()
    lecture_location = models.TextField()
    lecturer = models.TextField()
    lecturer_introduction = models.TextField()
    target_class = models.ManyToManyField(Class, blank=True)
    did_draw = models.BooleanField(blank=False, default=False)

    class Meta:
        ordering = ['-lecture_time']

    def get_absolute_url(self):
        return reverse("lecture:detail", kwargs={"id": self.id})

    def __str__(self):
        return self.title

    @property
    def get_number_of_selected(self):
        results = DrawResult.objects.all().filter(lecture=self)
        if self.did_draw:
            return len(results.filter(draw_status=DrawResult.Status.WIN))
        else:
            return len(results)


class AttendanceLog(models.Model):

    lecture = models.OneToOneField(Lecture, on_delete=models.CASCADE)
    student = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    didAttend = models.BooleanField('Attendance', default=False)

    def __str__(self):
        return self.lecture.title + ": " + self.student.username + ' Attend: ' + self.didAttend

    class Meta:
        ordering = ['student']


class DrawResult(models.Model):
    lecture = models.ForeignKey(Lecture, on_delete=models.CASCADE,unique=False,primary_key=False)
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,unique=False,primary_key=False)

    class Meta:
        unique_together = ('lecture', 'student')
        ordering = ['lecture']

    class Status(models.TextChoices):
        PENDING = 'PEN',_('Pending')
        WIN = 'WIN',_("Win")
        MISSED = 'MIS',_('Missed')

    draw_status = models.CharField(max_length=3, choices=Status.choices, default=Status.PENDING, null=False)

    def get_status(self):
        if self.draw_status == self.Status.WIN:
            return "中选"
        elif self.draw_status == self.Status.MISSED:
            return "落选"
        elif self.draw_status == self.Status.PENDING:
            return "等待抽选"
        else:
            raise KeyError

    def __str__(self):
        return str(self.lecture) + '-' + str(self.student) + '-' + self.get_status()
