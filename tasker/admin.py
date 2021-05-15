# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class UserAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'username',
        'first_name',
        'last_name',
        'email',
        'password',
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'image',
    )
    list_filter = (
        'last_login',
        'is_superuser',
        'is_staff',
        'is_active',
        'date_joined',
        'id',
        'password',
        'last_login',
        'is_superuser',
        'username',
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
        'date_joined',
        'image',
    )
    raw_id_fields = ('groups', 'user_permissions')


class DepartmentAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description')
    list_filter = ('id', 'name', 'description')
    # raw_id_fields = ('members', 'head')
    search_fields = ('name',)


class TaskAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'description',
        'created_on',
        'due_on',
        'state',
        'creator',
        'assignee',
    )
    list_filter = (
        'created_on',
        'due_on',
        'creator',
        'assignee',
        'id',
        'name',
        'description',
        'created_on',
        'due_on',
        'state',
        'creator',
        'assignee',
    )
    raw_id_fields = ('department',)
    search_fields = ('name',)


class DepartmentFileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'file',
        'department',
        'uploader',
        'upload_date',
        'description',
    )
    list_filter = (
        'department',
        'uploader',
        'upload_date',
        'id',
        'file',
        'department',
        'uploader',
        'upload_date',
        'description',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.User, UserAdmin)
_register(models.Department, DepartmentAdmin)
_register(models.Task, TaskAdmin)
_register(models.DepartmentFile, DepartmentFileAdmin)
