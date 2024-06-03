from django.db.models import Count
from django.contrib.auth.models import User
from dashboard.models import *
from projects.models import *
import datetime

class ChartJsData:
    
    def get_users_statistics(self, start_date=None, end_date=None):
        if not start_date or not end_date:
            raise ValueError("Both start_date and end_date must be provided.")

        admin_role = Role.objects.get(name='Admin')
        manager_role = Role.objects.get(name='Manager')

        end_date = end_date + datetime.timedelta(days=1)

        admin_count = User.objects.filter(role=admin_role, date_joined__range=(start_date, end_date)).count()
        manager_count = User.objects.filter(role=manager_role, date_joined__range=(start_date, end_date)).count()
        employee_count = User.objects.exclude(is_staff=True).exclude(role=admin_role).exclude(role=manager_role).filter(date_joined__range=(start_date, end_date)).count()

        # Get project counts based on status
        ongoing_projects_count = Projects.objects.filter(created_at__range=(start_date, end_date), status='ongoing').count()
        completed_projects_count = Projects.objects.filter(created_at__range=(start_date, end_date), status='completed').count()

        return {
            'admin_count': admin_count,
            'manager_count': manager_count,
            'employee_count': employee_count,
            'ongoing_projects_count': ongoing_projects_count,
            'completed_projects_count': completed_projects_count,
        }
    
    def get_projects_statistics(self, start_date=None, end_date=None):
        if not start_date or not end_date:
            raise ValueError("Both start_date and end_date must be provided.")

        ongoing_projects_count = Projects.objects.filter(created_at__range=(start_date, end_date), status='ongoing').count()
        completed_projects_count = Projects.objects.filter(created_at__range=(start_date, end_date), status='completed').count()

        return {
            'ongoing_projects_count': ongoing_projects_count,
            'completed_projects_count': completed_projects_count,
        }
    
    def get_tasks_statistics_by_project(self, start_date=None, end_date=None, project_id=None):
        if not start_date or not end_date:
            raise ValueError("Both start_date and end_date must be provided.")

        tasks = Tasks.objects.filter(created_at__range=(start_date, end_date))

        tasks_statistics_by_project = {}

        if project_id == 'all_projects':
            todo_tasks_count = tasks.filter(status='todo').count()
            inprogress_tasks_count = tasks.filter(status='inprogress').count()
            completed_tasks_count = tasks.filter(status='completed').count()

            tasks_statistics_by_project['all_projects'] = {
                'todo_tasks_count': todo_tasks_count,
                'inprogress_tasks_count': inprogress_tasks_count,
                'completed_tasks_count': completed_tasks_count,
            }
        elif project_id:
            project_tasks = tasks.filter(project_id=project_id)
            todo_tasks_count = project_tasks.filter(status='todo').count()
            inprogress_tasks_count = project_tasks.filter(status='inprogress').count()
            completed_tasks_count = project_tasks.filter(status='completed').count()

            tasks_statistics_by_project[project_id] = {
                'todo_tasks_count': todo_tasks_count,
                'inprogress_tasks_count': inprogress_tasks_count,
                'completed_tasks_count': completed_tasks_count,
            }

        return tasks_statistics_by_project
