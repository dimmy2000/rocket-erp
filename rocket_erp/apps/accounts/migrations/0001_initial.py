# Generated by Django 3.2.3 on 2021-05-31 10:28
import django.db.models.deletion
import django.utils.timezone
from django.db import migrations
from django.db import models

import rocket_erp.apps.accounts.models



def apply_migration(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    Group.objects.bulk_create([
        Group(name='Начальник производства'),
        Group(name='Администратор-сметчик'),
        Group(name='Снабженец-кладовщик'),
        Group(name='Конструктор'),
        Group(name='Маляр')
    ])


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="Account",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("password",
                 models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="first name"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, verbose_name="last name"
                    ),
                ),
                (
                    "is_staff",
                    models.BooleanField(
                        default=False,
                        help_text="Designates whether the user can log into this admin site.",
                        verbose_name="staff status",
                    ),
                ),
                (
                    "is_active",
                    models.BooleanField(
                        default=True,
                        help_text="Designates whether this user should be treated as active. Unselect this instead of deleting accounts.",
                        verbose_name="active",
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True,
                        verbose_name="email address"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="avatars/",
                        verbose_name="avatar",
                    ),
                ),
                (
                    "second_name",
                    models.CharField(
                        blank=True, max_length=50, null=True,
                        verbose_name="surname"
                    ),
                ),
                (
                    "about",
                    models.TextField(
                        blank=True,
                        max_length=350,
                        null=True,
                        verbose_name="description",
                    ),
                ),
                (
                    "birthday",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="birthday"
                    ),
                ),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=11, null=True,
                        verbose_name="phone"
                    ),
                ),
                (
                    "is_deleted",
                    models.BooleanField(default=False, verbose_name="deleted"),
                ),
                (
                    "updated",
                    models.DateTimeField(auto_now=True,
                                         verbose_name="updated"),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.Permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "user",
                "verbose_name_plural": "users",
                "abstract": False,
            },
            managers=[
                ("objects", rocket_erp.apps.accounts.models.UserManager()),
            ],
        ),
        migrations.RunPython(apply_migration),
    ]
