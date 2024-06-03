from django.urls import path
from . import views
urlpatterns =[
    path('login/', views.LoginView.as_view(), name='login'),
    path('dashboard/', views.DashboardView.as_view(), name='dashboard'),
    path('users/', views.UsersView.as_view(), name='users'),
    path('project_statistics/', views.ProjectStatisticsView.as_view(), name='project_statistics'),
    path('tasks_listing/', views.TasksListingView.as_view(), name='tasks_listing'),
    path('projects_listing/', views.ProjectsListingView.as_view(), name='projects_listing'),

]
 