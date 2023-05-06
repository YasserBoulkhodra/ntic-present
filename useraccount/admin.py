from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import *

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'last_name', 'email', 'phone', 'is_teacher', 'is_student', 'is_headdep','grade','level')
    list_filter = ('username', 'is_teacher', 'is_student', 'is_headdep')
    def level(self, obj):
        if obj.is_student:
            return obj.level
        return None

    def grade(self, obj):
        if obj.is_teacher:
            return obj.grade
        return None
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'email', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions', 'is_teacher', 'is_student', 'is_headdep')}),
    )
    
admin.site.register(User, CustomUserAdmin)
admin.site.register(Student)
admin.site.register(Teacher)