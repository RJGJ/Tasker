from django.contrib.auth.base_user import AbstractBaseUser
from django.core.checks.messages import Error
from django.db.models.query import QuerySet
from django.db.models.query_utils import Q
from django.forms.utils import ErrorDict
from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.http.request import HttpRequest

from allauth.account.decorators import login_required

from .models import *
from .forms import *
from .test_functions import *


# Create your views here.def index(request):
def index(request):
    return render(request, 'index/index.html', {})


@login_required
def dashboard(request):
    user_id = request.user.id
    user_departments = Department.objects.filter(members__in=[user_id])
    tasks = Task.objects.filter(department__in=user_departments)
    context = {
        'tasks': tasks,
        'departments': user_departments,
    }
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def account_settings(request):
    form = UserForm(instance=request.user)
    errors = None

    if request.method == 'POST':
        form = UserForm(request.POST or None,
                        request.FILES or None, instance=request.user)
        if form.is_valid():
            form.save()
        else:
            errors = form.errors

    return render(request, 'account/account-settings.html', {
        'form': form,
        'errors': errors
    })


@login_required
def department(request, dept_id):
    department = Department.objects.get(id=dept_id)
    tasks = Task.objects.filter(department__in=[department.id])
    files = DepartmentFile.objects.filter(department=department)
    context = {
        'department': department,
        'tasks': tasks,
        'files': files,
    }
    return render(request, 'dashboard/department.html', context)


@login_required
def task(request, dept_id, task_id=None):
    dept = Department.objects.get(id=dept_id)
    form = TaskForm()
    task = None
    errors: ErrorDict = ErrorDict()

    if not task_id == None:
        task = Task.objects.get(id=task_id)
        form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.department.add(dept)
            obj.creator = request.user
            obj.save()

            return redirect(department, dept.id)

        else:
            errors = form.errors
    context = {
        'form': form,
        'task': task,
        'errors': errors,
        'dept_id': dept_id,
    }

    return render(request, 'dashboard/task_v2.html', context)


@login_required
def delete_task(request, id):
    tsk = Task.objects.get(id=id)

    if request.method == 'POST':
        option = request.POST['option']
        option = option.lower().strip()  # clean the string

        if option == 'delete':
            tsk.delete()
            return redirect(dashboard)

        elif option == 'cancel':
            return redirect(task, tsk.id)

    return render(request, 'dashboard/delete-item.html', {'item': tsk})


@login_required
def proper_names(request: HttpRequest, department_id: int) -> JsonResponse:
    dept: Department = Department.objects.get(id=department_id)
    users: QuerySet[User] = dept.members.all()

    names: dict = {}

    user: User
    for user in users:
        names[user.pk] = user.username

        if user.first_name and user.last_name:
            names[user.pk] = f'{user.first_name} {user.last_name}'

    data = {
        'message': 'hello',
        'names': names,
    }
    return JsonResponse(data)


@login_required
def task_feed(request: HttpRequest):
    user = request.user
    tasks = Task.objects.filter(
        Q(assignee__in=[user]) |
        Q(department__head__in=[user])
    ).exclude(state='DONE')

    context = {
        'tasks': tasks,
    }
    return render(request, 'dashboard/task-feed.html', context)


# API
@login_required
def change_state(request, state: int, task_id: int):

    states = {
        0: 'TODO',
        1: 'DOING',
        2: 'DONE',
    }

    task: Task = Task.objects.get(id=task_id)
    new_state = states[state]
    task.state = new_state
    task.save()

    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


@login_required
def add_file(request: HttpRequest, department_id: int):
    dep: Department = Department.objects.get(id=department_id)
    form = DepartmentFileForm()
    errors: ErrorDict = ErrorDict()

    if request.method == 'POST':
        form = DepartmentFileForm(
            request.POST or None, request.FILES or None, instance=None)

        if form.is_valid():
            obj: DepartmentFile = form.save(commit=False)
            obj.uploader = request.user
            obj.department = dep
            obj.save()

            return redirect(department, dep.pk)

        else:
            errors = form.errors

    context = {
        'errors': errors,
        'form': form,
    }
    return render(request, 'dashboard/upload-file.html', context)
