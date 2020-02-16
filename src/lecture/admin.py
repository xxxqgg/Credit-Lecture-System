from django.contrib import admin
from .models import (Lecture, AttendanceLog, DrawResult)


# Register your models here.
class LectureAdmin(admin.ModelAdmin):
    save_as = True


admin.site.register(Lecture, LectureAdmin)
admin.site.register(AttendanceLog)
admin.site.register(DrawResult)
