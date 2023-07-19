from django.core.exceptions import ValidationError


def validate_only_letters(value):
    for el in value:
        if not el.isalpha():
            raise ValidationError('Only letters are allowed in this section!')