from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('account-settings/', account_settings, name='account_settings'),
    path('task/<int:dept_id>/<int:task_id>/', task, name='task'),
    path('task/<int:dept_id>/', task, name='task'),
    path('delete-task/<int:id>/', delete_task, name='delete_task'),
    path('department/<int:dept_id>', department, name='department'),
    path('change-state/<int:state>/<int:task_id>/',
         change_state, name='change_state'),
    path('task-feed', task_feed, name='task_feed'),
    path('add-file/<int:department_id>/', add_file, name='add_file'),
]

# API
urlpatterns += [
    path('api/proper-names/<int:department_id>/',
         proper_names, name='proper_names'),
    path('api/get-tasks/<int:department_id>/', get_tasks, name="get_tasks"),
]
