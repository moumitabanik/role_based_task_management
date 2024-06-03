from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    PermissionsMixin,
)

class Role(models.Model):
    name = models.CharField(
        verbose_name="Name", max_length=50, unique=True, help_text="User role name"
    )
    description = models.TextField(
        verbose_name="Description", blank=True, help_text="User role description"
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "role"
        verbose_name = "Role"
        verbose_name_plural = "Roles"
        ordering = ("name",)


class UserManager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, password=None, **kwargs):
        if not username:
            raise ValueError("User must have a username")
        user = self.model(
            username=username,
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **kwargs,
        )
        user.set_password(password)
        user.is_admin = False
        user.is_staff = False
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, first_name, last_name, password=None, **kwargs):
        user = self.create_user(username, email, first_name, last_name, password, **kwargs)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        # role is an instance of Role model
        owner = Role.objects.get(name="Admin")
        user.role = owner
        if user.is_staff and user.is_admin is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if user.is_superuser is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    username = models.CharField(
        "username",
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=100)
    is_active = models.BooleanField(
        "active",
        default=True,
        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
    )
    email = models.EmailField("email address", blank=True)
    is_staff = models.BooleanField(
        "staff status",
        default=False,
        help_text="Designates whether the user can log into this admin site.",
    )
    is_superuser = models.BooleanField("superuser status", default=False)
    is_admin = models.BooleanField(
        "admin status",
        default=False,
        help_text="Designates whether the user is admin or not",
    )
    role = models.ForeignKey(
        Role,
        verbose_name="Role",
        related_name="users",
        null=True,
        on_delete=models.SET_NULL,
        help_text="Role",
    )
    date_joined = models.DateTimeField("date joined", default=timezone.now)
    last_modified = models.DateTimeField(auto_now=True)
    objects = UserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["first_name", "last_name", "email", "password"]

    class Meta:
        db_table = "user"
        verbose_name = "Users"
        verbose_name_plural = "Users"

    def get_full_name(self):
        """Return the first_name plus the last_name, with a space in between."""
        full_name = f"{self.first_name} {self.last_name}"
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self):
        role_name = self.role.name if self.role else None
        if role_name in ["Admin", "Manager", "Employee"]:
            return self.username

    def has_perm(self, perm, obj=None):
        return True

    def is_user_staff(self):
        return self.is_staff
