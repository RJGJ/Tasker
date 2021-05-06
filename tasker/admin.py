from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Department)
admin.site.register(Task)
admin.site.register(TaskItem)
admin.site.register(Submition)
admin.site.register(SubmitionFile)# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class UserAdmin(admin.ModelAdmin):

    list_display = (
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
    raw_id_fields = ('members', 'head')
    search_fields = ('name',)


class TaskAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'created_on', 'due_on')
    list_filter = (
        'created_on',
        'due_on',
        'id',
        'name',
        'description',
        'created_on',
        'due_on',
    )
    raw_id_fields = ('department',)
    search_fields = ('name',)


class TaskItemAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'description', 'done', 'task')
    list_filter = (
        'done',
        'task',
        'id',
        'name',
        'description',
        'done',
        'task',
    )
    search_fields = ('name',)


class SubmitionAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'pub_date',
        'title',
        'description',
        'approved',
        'task',
        'goal',
    )
    list_filter = (
        'user',
        'pub_date',
        'approved',
        'task',
        'goal',
        'id',
        'user',
        'pub_date',
        'title',
        'description',
        'approved',
        'task',
        'goal',
    )


class SubmitionFileAdmin(admin.ModelAdmin):

    list_display = ('id', 'file', 'submition_parent')
    list_filter = ('submition_parent', 'id', 'file', 'submition_parent')


def _register(model, admin_class):
    admin.site.register(model, admin_class)


def _unregister(model):
    admin.site.unregister(model)


_unregister(models.User)
_unregister(models.Department)
_unregister(models.Task)
_unregister(models.TaskItem)
_unregister(models.Submition)
_unregister(models.SubmitionFile)


_register(models.User, UserAdmin)
_register(models.Department, DepartmentAdmin)
_register(models.Task, TaskAdmin)
_register(models.TaskItem, TaskItemAdmin)
_register(models.Submition, SubmitionAdmin)
# _register(models.SubmitionFile, SubmitionFileAdmin)
