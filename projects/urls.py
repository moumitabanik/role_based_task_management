from django.urls import path
from .views import *

urlpatterns = [
    path('projects/', ProjectListCreateView.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectRetrieveUpdateDestroyView.as_view(), name='project-detail'),
    path('tasks-add/', TaskCreateView.as_view(), name='task-list-create'),
    path('tasks_listing/', TaskListView.as_view(), name='tasks_listing'),
    path('tasks/<int:pk>/', TaskRetrieveUpdateDestroyView.as_view(), name='task-detail'),
    path('<int:project_id>/tasks/', ProjectTasksAPI.as_view(), name='project_tasks_api'),
    path('get-chart-data/', GetChartJsData.as_view(), name='get-chart-data'),
    path('tasks/user/', TaskListByUserView.as_view(), name='user-task-list'),
    path('tasks/<int:pk>/update/', TaskUpdateStatusView.as_view(), name='task-update-status'),
    path('notifications/', UserNotificationsView.as_view(), name='notifications'),
    path('get-project-data/', GetProjectChartJsData.as_view(), name='get-project-data'),
]