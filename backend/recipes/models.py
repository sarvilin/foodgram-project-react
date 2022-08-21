from django.db import models

from users.models import User


class Recipe(models.Model):
    name = models.CharField(
        'Название',
        max_length=200,
        # choices=ROLE_CHOICES,
        # default=USER,
        blank=True
    )
    text = models.TextField(
        'Описание',
        max_length=200,
        # choices=ROLE_CHOICES,
        # default=USER,
        blank=True
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes'
    )

    def __str__(self):
        return self.text
