from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', dashboard, name='dashboard'),
    path('account-settings/', account_settings, name='account_settings'),
    # path('new_task/<int:dept_id>/', new_task, name='new_task'),
    # path('task/<int:id>/', task, name='task'),
    path('task/<int:dept_id>/<int:task_id>/', task, name='task'),
    path('task/<int:dept_id>/', task, name='task'),
    # path('delete-goal/<int:id>/', delete_goal, name='delete_goal'),
    path('delete-task/<int:id>/', delete_task, name='delete_task'),
    # path('create-submition/<int:task_id>/<int:goal_id>/', create_submition, name='create_submition'),
    # path('goal-form/<int:id>/', goal_form, name='goal_form'),
    # path('new-goal/<int:task_id>/<str:title>', new_goal, name='new-goal'),
    # path('accept-submition/<int:task_id>/<int:submition_id>/', accept_submition, name='accept_submition'),
    path('department/<int:dept_id>', department, name='department'),
    path('change-state/<int:state>/<int:task_id>/', change_state, name='change_state'),
    path('task-feed', task_feed, name='task_feed'),
]

# API
urlpatterns += [
    path('api/proper-names/<int:department_id>', proper_names, name='proper_names'),
]
