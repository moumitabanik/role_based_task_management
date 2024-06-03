from django.views.generic.base import View
from django.shortcuts import render
from django.views.decorators.cache import never_cache
from django.utils.decorators import method_decorator
from django.contrib.staticfiles import finders
from django.http import HttpResponse
from django.contrib.staticfiles import finders


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/login.html")
    @method_decorator(never_cache)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)
    
class DashboardView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/dashboard.html")
    
class UsersView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/users.html")
    
class ProjectStatisticsView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/project_statistics.html")
    
class TasksListingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/tasks_listing.html")

class ProjectsListingView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "pages/projects_listing.html")