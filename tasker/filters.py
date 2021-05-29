import django_filters
from django_filters.filters import CharFilter

from .models import *


class TaskFilter(django_filters.FilterSet):
    creation_date = django_filters.DateFilter(
        field_name='created_on', lookup_expr='gte', label='Creation Date is later than or on:')

    target_date = django_filters.DateFilter(
        field_name='due_on', lookup_expr='lte', label='Target Date is earlier than or on:')

    name = CharFilter(field_name='name', lookup_expr='icontains')

    state = django_filters.ChoiceFilter(
        field_name='state', choices=Task.choices)

    class Meta:
        model = Task
        fields = ['name', 'state']
