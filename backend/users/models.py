# from django.contrib.auth.models import AbstractUser
# # from django.core.validators import MinValueValidator, MaxValueValidator
# from django.db import models
#
# # from reviews.validators import validate_year
#
# USER = 'user'
# ADMIN = 'admin'
#
# ROLE_CHOICES = [
#     (USER, USER),
#     (ADMIN, ADMIN),
# ]
#
#
# class User(AbstractUser):
#     """Модель для создания таблицы Пользователи."""
#
#     email = models.EmailField(
#         max_length=254,
#         unique=True,
#         blank=False,
#         null=False
#     )
#     role = models.CharField(
#         'роль',
#         max_length=20,
#         choices=ROLE_CHOICES,
#         default=USER,
#         blank=True
#     )
#     bio = models.TextField(
#         'биография',
#         blank=True,
#     )
#     confirmation_code = models.CharField(
#         'код подтверждения',
#         max_length=255,
#         null=True,
#         blank=False,
#         default='XXXX'
#     )
#
#     class Meta:
#         ordering = ('id',)
#         verbose_name = 'Пользователь'
#         verbose_name_plural = 'Пользователи'
#
#     @property
#     def is_user(self):
#         return self.role == USER
#
#     @property
#     def is_admin(self):
#         return self.role == ADMIN
#
#     def __str__(self):
#         return self.username
