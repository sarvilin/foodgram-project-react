from re import compile

from django.core.exceptions import ValidationError
from django.utils.deconstruct import deconstructible


@deconstructible
class OneOfTwoValidator:
    first_regex = '[^а-яёА-ЯЁ]+'
    second_regex = '[^a-zA-Z]+'
    message = (
        'Переданное значение на разных языках либо содержит что-то кроме букв.'
    )

    def __init__(self, first_regex=None, second_regex=None, message=None):
        if first_regex is not None:
            self.first_regex = first_regex
        if second_regex is not None:
            self.second_regex = second_regex
        if message is not None:
            self.message = message

        self.first_regex = compile(self.first_regex)
        self.second_regex = compile(self.second_regex)

    def __call__(self, value):
        if self.first_regex.search(value) and self.second_regex.search(value):
            raise ValidationError(self.message)


@deconstructible
class MinLenValidator:
    min_len = 0
    message = 'Переданное значение слишком короткое.'

    def __init__(self, min_len=None, message=None):
        if min_len is not None:
            self.min_len = min_len
        if message is not None:
            self.message = message

    def __call__(self, value):
        if len(value) < self.min_len:
            raise ValidationError(self.message)
