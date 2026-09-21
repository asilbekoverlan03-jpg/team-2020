from rest_framework import serializers
from .models import Task, Subtask, TaskFile, Comment


class SubtaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subtask
        fields = ["id", "task", "title", "completed"]


class TaskFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskFile
        fields = ["id", "task", "file"]


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "task", "user", "text", "created_date"]


class TaskSerializer(serializers.ModelSerializer):
    subtasks = SubtaskSerializer(many=True, read_only=True)
    files = TaskFileSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)

    progress = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    overdue = serializers.SerializerMethodField()

    class Meta:
        model = Task
        fields = ["id", "title", "description", "completed", "priority",
                  "deadline", "created_date", "project", "assignee", "tags",
                  "subtasks", "files", "comments",
                  "progress", "comments_count", "overdue"]

    def get_progress(self, obj):
        return obj.get_progress()

    def get_comments_count(self, obj):
        return obj.get_comments_count()

    def get_overdue(self, obj):
        return obj.is_overdue()