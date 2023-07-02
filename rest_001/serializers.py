from rest_framework import serializers
from auth_001.models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ('id', 'name', 'description', 'create_date', 'date_done', 'is_important', 'user')
        read_only_fields = ('create_date',)