from .views import *
from django.urls import path
from knox import views as knox_views

urlpatterns = [
    path('roles/', RoleCreateView.as_view(), name='role-create'),
    path("register/", RegisterAPI.as_view(), name="register-user"),
    path("login/", LoginAPI.as_view(), name="login"),
    path("users_list/", UsersList.as_view(), name="users_list"),
    path("logout/", knox_views.LogoutView.as_view(), name="logout"),
]