from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LectureUser, Class
# Register your models here.


admin.site.register(LectureUser, UserAdmin)
admin.site.register(Class)