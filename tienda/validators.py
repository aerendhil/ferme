from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

def validate_password(value):
    print('suuuuuuuuuuuuuup!')
    if value != 'a':
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value}
        )
    return value