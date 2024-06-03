from django.db import models
from dashboard.models import User
from django.utils import timezone
# Create your models here.

class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=[('ongoing', 'Ongoing'), ('completed', 'Completed')])
    created_at = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "projects"

class Tasks(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('todo', 'To Do'), ('inprogress', 'In Progress'), ('completed', 'Completed')])
    deadline = models.DateField()
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "tasks"