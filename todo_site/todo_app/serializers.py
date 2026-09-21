from rest_framework import serializers
from .models import Task, Subtask, TaskFile, Comment


# Маленькие сериализаторы: «как показать подзадачу / файл / комментарий»
class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = "all"        # все поля модели


class TaskFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFile
        fields = "all"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "all"


class TaskSerializer(serializers.ModelSerializer):
    # вложенные списки; read_only = только показываем, создавать через них нельзя
    subtasks = SubtaskSerializer(many=True, read_only=True)
    files = TaskFileSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    # значения из методов модели
    progress = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    overdue = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = "all"        # title, description, completed, priority,
        # deadline, project, assignee, tags ...

    # для поля progress DRF сам ищет метод get_progress
    def get_progress(self, obj):
        return obj.get_progress()

    def get_comments_count(self, obj):
        return obj.get_comments_count()

    def get_overdue(self, obj):
        return obj.is_overdue()