from django.contrib.auth.base_user import AbstractBaseUser
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
        form = UserForm(request.POST or None, request.FILES or None, instance=request.user)
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
    context = {
        'department': department,
        'tasks': tasks,
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
        option = option.lower().strip() # clean the string

        if option == 'delete':
            tsk.delete()
            return redirect(dashboard)
        
        elif option == 'cancel':
            return redirect(task, tsk.id)


    return render(request, 'dashboard/delete-item.html', {'item': tsk})


@login_required
def proper_names(request:HttpRequest, department_id:int) -> JsonResponse:
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


# @login_required
# def delete_goal(request, id):
#     goal = TaskItem.objects.get(id=id)
#     g_task = goal.task.all()[0]
    
#     if request.method == 'POST':
#         option = request.POST['option']
#         option = option.lower().strip() # clean the string

#         if option == 'delete':
#             goal.delete()
#             return redirect(task, g_task.id)
        
#         elif option == 'cancel':
#             return redirect(task, g_task.id)

#     return render(request, 'dashboard/delete-item.html', {'item': goal})


# @login_required
# def add_files(request, submition_id):
#     pass


# @login_required
# def create_submition(request, task_id, goal_id):
#     form = SubmitionForm()
#     errors = None

#     if request.method == 'POST':
#         form = SubmitionForm(request.POST or None)

#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.user = request.user
#             goal_obj = TaskItem.objects.get(id=goal_id)
#             obj.goal = goal_obj
#             obj.task = Task.objects.get(id=task_id)
#             obj.save()

#             return redirect(task, task_id)

#         else:
#             errors = form.errors

#     context = {
#         'errors': errors,
#         'form': form,
#     }

#     return render(request, 'dashboard/create-submition.html', context)


# @login_required
# def goal_form(request, id):
#     goal = TaskItem.objects.get(id=id)
#     form = GoalForm(instance=goal)
#     errors = None

#     if request.method == 'POST':
#         if form.is_valid:
#             form = GoalForm(request.POST or None, instance=goal)
#             obj = form.save()
#             task_obj = obj.task

#             return redirect(task, task_obj.id)
        
#         else:
#             errors = form.errors
#             print(errors)

#     context = {
#         'errors': errors,
#         'form': form,
#     }

#     return render(request, 'dashboard/goal-form.html', context)


# @login_required
# def new_goal(request, task_id, title):

#     new_goal_obj = TaskItem(name=title)
#     new_goal_obj.task = Task.objects.get(id=task_id)
#     new_goal_obj.save()

#     return redirect(task, task_id)


# @login_required
# def accept_submition(request, task_id, submition_id):

#     submition_obj = Submition.objects.get(id=submition_id)
#     submition_obj.approved = True
#     submition_obj.save()

#     goal_obj = submition_obj.goal
#     goal_obj.done = True
#     goal_obj.save()

#     return redirect(task, task_id)


@login_required
def task_feed(request:HttpRequest):
    user = request.user
    tasks = Task.objects.filter(
        Q(assignee__in=[user]) |
        Q(department__head__in=[user])
    )

    print(tasks)

    context = {
        'tasks': tasks,
    }
    return render(request, 'dashboard/task-feed.html', context)


# API
@login_required
def change_state(request, state:int, task_id:int):

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
