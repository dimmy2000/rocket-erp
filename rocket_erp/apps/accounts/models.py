from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.db.models import BooleanField
from django.db.models import CASCADE
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import EmailField
from django.db.models import ForeignKey
from django.db.models import ImageField
from django.db.models import Model
from django.db.models import TextField


class UserManager(BaseUserManager):

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)

        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email, password, **extra_fields)


class Account(AbstractUser):

    username = None
    email = EmailField("email address", unique=True)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    avatar = ImageField(
        upload_to="avatars/", blank=True, null=True, verbose_name="avatar"
    )

    second_name = CharField(
        blank=True, verbose_name="surname", null=True, max_length=50
    )

    about = TextField(
        blank=True, verbose_name="description", null=True, max_length=350
    )

    birthday = DateTimeField(null=True, blank=True, verbose_name="birthday")

    phone = CharField(
        max_length=11, null=True, blank=True, verbose_name="phone"
    )

    is_deleted = BooleanField(default=False, verbose_name="deleted")

    updated = DateTimeField(auto_now=True, verbose_name="updated")

    objects = UserManager()

    def __str__(self):
        return " ".join([self.first_name, self.last_name])


class Activation(Model):
    user = ForeignKey(Account, on_delete=CASCADE)
    created_at = DateTimeField(auto_now_add=True)
    code = CharField(max_length=20, unique=True)
    email = EmailField(blank=True)
