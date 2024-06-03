from rest_framework import serializers
from .models import Projects, Tasks
from dashboard.models import User
from notifications.models import Notification


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Projects
        fields = '__all__'

class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = "__all__"

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields ='__all__'

class TaskAjaxSerializer(serializers.ModelSerializer):
    assigned_to_username = serializers.SerializerMethodField()
    created_by_username = serializers.SerializerMethodField()
    project_name = serializers.SerializerMethodField()

    class Meta:
        model = Tasks
        fields ='__all__'
    
    def get_assigned_to_username(self, obj):
        if isinstance(obj, dict):
            return obj.get('assigned_to', {}).get('username') if obj.get('assigned_to') else None
        elif hasattr(obj, 'assigned_to'):
            return obj.assigned_to.username if obj.assigned_to else None
        return None

    def get_created_by_username(self, obj):
        if isinstance(obj, dict):
            return obj.get('created_by', {}).get('username') if obj.get('created_by') else None
        elif hasattr(obj, 'created_by'):
            return obj.created_by.username if obj.created_by else None
        return None

    def get_project_name(self, obj):
        if isinstance(obj, dict):
            return obj.get('project', {}).get('name') if obj.get('project') else None
        elif hasattr(obj, 'project'):
            return obj.project.name if obj.project else None
        return None


class ChartSerializer(serializers.ModelSerializer):
    data = serializers.JSONField()

class NotificationSerializer(serializers.ModelSerializer):
    actor_username = serializers.SerializerMethodField()

    def get_actor_username(self, obj):
        actor_id = obj.actor_object_id
        try:
            user = User.objects.get(id=actor_id)
            return user.username
        except User.DoesNotExist:
            return None

    class Meta:
        model = Notification
        fields = ['actor_object_id', 'verb', 'actor_username']