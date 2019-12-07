from django.contrib import admin
from .models import (Lecture, AttendanceLog, DrawResult)
# Register your models here.

admin.site.register(Lecture)
admin.site.register(AttendanceLog)
admin.site.register(DrawResult)