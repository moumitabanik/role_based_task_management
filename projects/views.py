from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Projects, Tasks
from dashboard.models import User
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .custom_permissions import IsAdminOrManager, IsAdminUser
from .charts import ChartJsData
import datetime
from notifications.signals import notify

class ProjectListCreateView(generics.ListCreateAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]

class ProjectRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Projects.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]

class TaskListView(generics.ListAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskAjaxSerializer
    permission_classes = [IsAuthenticated]

class TaskCreateView(generics.CreateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskCreateSerializer
    permission_classes = [IsAuthenticated,IsAdminOrManager]
    
    def perform_create(self, serializer):
        task = serializer.save()
        self.send_notification(task)

    def send_notification(self, task):
        assigned_user = task.assigned_to
        admin_manager_users = User.objects.filter(is_staff=True)
        
        # Notify assigned user
        notify.send(
            self.request.user,
            recipient=assigned_user,
            verb=f'You have been assigned a new task: {task.name}',
            target=task
        )
        
        # Notify admin and manager users
        notify.send(
            self.request.user,
            recipient=admin_manager_users,
            verb=f'Task {task.name} has been created and assigned to {assigned_user.username}',
            target=task
        )
    
class TaskRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated, IsAdminOrManager]

class GetChartJsData(APIView):
    permission_classes = [IsAdminUser]

    def get(self, request):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')

        try:
            start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response("Invalid date format. Please use 'YYYY-MM-DD' format for dates.", status=status.HTTP_400_BAD_REQUEST)

        instance = ChartJsData()
        statistics_users = instance.get_users_statistics(start_date=start_date, end_date=end_date)
        statistics_projects = instance.get_projects_statistics(start_date=start_date, end_date=end_date)

        # Combine both statistics into one dictionary
        combined_statistics = {**statistics_users, **statistics_projects}

        return Response(combined_statistics, status=status.HTTP_200_OK)
    
class GetProjectChartJsData(APIView):
    permission_classes = [IsAdminOrManager]

    def get(self, request):
        start_date_str = request.query_params.get('start_date')
        end_date_str = request.query_params.get('end_date')
        project_id = request.query_params.get('project_id')

        try:
            start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
            end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()
        except ValueError:
            return Response("Invalid date format. Please use 'YYYY-MM-DD' format for dates.", status=status.HTTP_400_BAD_REQUEST)

        instance = ChartJsData()
        statistics_projects = instance.get_tasks_statistics_by_project(start_date=start_date, end_date=end_date, project_id=project_id)

        return Response(statistics_projects, status=status.HTTP_200_OK)
    
class ProjectTasksAPI(APIView):
    def get(self, request, project_id):
        try:
            tasks = Tasks.objects.filter(project_id=project_id)
            serializer = TaskSerializer(tasks, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class TaskListByUserView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Tasks.objects.filter(assigned_to=user)
    
class TaskUpdateStatusView(generics.UpdateAPIView):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        task = self.get_object()
        old_status = task.status
        new_status = self.request.data.get('status')

        if old_status != new_status:
            serializer.save()

            # Send notification to admin and manager
            admin_manager_users = User.objects.filter(is_staff=True)
            task_id = task.id
            notify.send(
                self.request.user,
                recipient=admin_manager_users,
                verb=f'Task {task_id}: status changed from {old_status} to {new_status}',
                target=task
            )
        else:
            serializer.save()

class UserNotificationsView(generics.ListAPIView):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Notification.objects.filter(recipient=user).order_by('-timestamp')