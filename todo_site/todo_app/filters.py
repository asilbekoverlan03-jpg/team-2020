import django_filters
from .models import Task, Project


class TaskFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(field_name='project__category')
    project = django_filters.NumberFilter(field_name='project')

    class Meta:
        model = Task
        fields = ['category', 'project']


class ProjectFilter(django_filters.FilterSet):
    category = django_filters.NumberFilter(field_name='category')

    class Meta:
        model = Project
        fields = ['category']