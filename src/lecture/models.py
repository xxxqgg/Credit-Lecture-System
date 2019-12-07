from django.db import models
from django.urls import reverse
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
        result = self.title
        result += "\nLecturer: " + self.lecturer
        result += '\nLecturer intro: ' + self.lecturer_introduction
        result += '\nIntroduction: ' + self.introduction
        result += '\nCapacity: ' + str(self.capacity)
        result += '\nLocation: ' + self.lecture_location
        result = result.replace('\n','<br/>')
        return result



