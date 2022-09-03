from django.contrib.auth.models import AbstractUser
from django.db.models import (CharField, EmailField,
                              ManyToManyField)
from django.db.models.functions import Length
from django.utils.translation import gettext_lazy

CharField.register_lookup(Length)


class MyUser(AbstractUser):
    email = EmailField(
        verbose_name='Email',
        max_length=200,
        unique=True,
        help_text='Email',
    )
    username = CharField(
        verbose_name='Имя пользователя',
        max_length=200,
        unique=True,
        help_text='Имя пользователя',
    )
    first_name = CharField(
        verbose_name='Имя',
        max_length=200,
        help_text='Имя',
    )
    last_name = CharField(
        verbose_name='Фамилия',
        max_length=200,
        help_text='Фамилия',
    )
    password = CharField(
        verbose_name=gettext_lazy('Пароль'),
        max_length=200,
        help_text='Пароль',
    )
    subscribe = ManyToManyField(
        verbose_name='Подписка',
        related_name='subscribers',
        to='self',
        symmetrical=False,
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('username',)

    def __str__(self):
        return f'{self.username}: {self.email}'
