from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import LectureUser, Class
# Register your models here.


class MyUserAdmin(UserAdmin):
    # The forms to add and change user instances
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('student_id','email', 'is_staff')
    list_filter = ('is_staff',)
    fieldsets = (
        (None, {'fields': ('student_id', 'email', 'password','student_class')}),
        ('Permissions', {'fields': ('is_staff',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('student_id', 'email', 'password1', 'password2','student_class')}
        ),
    )
    search_fields = ('student_id',)
    ordering = ('student_id',)
    filter_horizontal = ()


admin.site.register(LectureUser, MyUserAdmin)
admin.site.register(Class)
