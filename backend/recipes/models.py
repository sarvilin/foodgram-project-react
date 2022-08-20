from django.contrib.auth import get_user_model
from django.db import models

# from users.models import User
User = get_user_model()


class Recipe(models.Model):
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='recipes'
    )

    def __str__(self):
        return self.text
