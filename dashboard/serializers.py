from django.contrib.auth import get_user_model
from rest_framework import serializers
from .models import Role, User
from knox.models import AuthToken
from django.contrib.auth.hashers import make_password

User = get_user_model()

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    role = RoleSerializer(read_only=True)
    class Meta:
        model = User
        fields = (
            "id",
            "email",
            "role",
            "username",
            "first_name",
            "last_name",
        )

class UserAjaxSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="role.name", required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "role",
            "is_active",
            "email",
            "first_name",
            "last_name",
        )

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    role = serializers.CharField(source="role.name", required=False)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "role",
            "password",
        )
        extra_kwargs = {"password": {"write_only": True}, "id": {"read_only": True}}

    def create(self, validated_data):
        # Extract and hash the password
        password = validated_data.pop("password")
        hashed_password = make_password(password)

        # Extract role data
        role_name = validated_data.pop("role", {}).get("name", "Employee")

        # Fetch or create the role
        role, _ = Role.objects.get_or_create(name=role_name)

        # Create the user instance
        user = User(**validated_data)
        user.password = hashed_password  # Set the hashed password
        user.role = role

        # Set additional attributes for admin role
        if role.name == "Admin":
            user.is_admin = True
            user.is_staff = True
            user.is_superuser = True
        
        # Save the user instance
        user.save()
        
        # Create a token for the user
        token_instance, token = AuthToken.objects.create(user)

        return user