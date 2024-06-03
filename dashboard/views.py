# Django
from django.http import JsonResponse
from django.contrib.auth import login, get_user_model

# REST Framework
from rest_framework import generics, permissions, status, viewsets
from rest_framework.response import Response
from rest_framework.authtoken.serializers import AuthTokenSerializer

# KNOX
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from knox.settings import knox_settings


# Serializers
from .serializers import *
from .models import Role 


User = get_user_model()

class IsAdminUser(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user and request.user.is_staff

class RoleCreateView(generics.CreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer

class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"requests": request})
        print(serializer)
        if serializer.is_valid():
            user = serializer.save()
            print(user)
            return Response(
                {
                    "user": UserSerializer(user, context=self.get_serializer_context()).data,
                    "token": AuthToken.objects.create(user)[1]
                }
            )
        else:
            username = request.data.get("username")
            if username:
                matched_user = User.objects.filter(username=username).first()
                if matched_user:
                    user_data = UserSerializer(matched_user, context=self.get_serializer_context()).data
                    token = AuthToken.objects.create(matched_user)[1]
                    user_data['token'] = token
                    user_data['message'] = "User already exists. Returning existing user details."
                    return Response(user_data, status=status.HTTP_409_CONFLICT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
    
class UsersList(generics.ListAPIView):
    serializer_class = UserAjaxSerializer

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset