import os
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError


def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1].lower()
    valid_extensions = ['.png', '.jpg', '.jpeg']
    if ext not in valid_extensions:
        raise ValidationError(
            _('File extension (%(ext)s) not allowed!'),
            params={'ext': ext},
            code='ext_not_allowed',
        )
