"""Custom fields."""

import re

from django import forms
from django.db import models
from django.utils.translation import ugettext_lazy as _ul

ARTICLE_RE = re.compile(r'^[a-zA-Z0-9- ]*$')


class ArticleField(models.CharField):
    """Article field."""

    description = _ul('Article string')

    def __init__(self, *args, **kwargs):
        """Override default max length."""
        defaults = {
            'max_length': 50,
        }
        defaults.update(kwargs)
        super(ArticleField, self).__init__(*args, **defaults)

    def formfield(self, **kwargs):
        """Add min value validation."""
        defaults = {
            'form_class': forms.RegexField,
            'regex': ARTICLE_RE,
            'max_length': self.max_length,
            'error_messages': {
                'invalid': _ul('Should contain only letters, digits, dashes and whitespaces'),
            },
        }
        defaults.update(kwargs)
        return super(ArticleField, self).formfield(**defaults)


class PositiveDecimalField(models.DecimalField):
    """Positive decimal model field."""

    description = _ul('Positive decimal number')

    def __init__(self, *args, **kwargs):
        """Override default decimal values."""
        defaults = {
            'max_digits': 10,
            'decimal_places': 2,
        }
        defaults.update(kwargs)
        super(PositiveDecimalField, self).__init__(*args, **defaults)

    def formfield(self, **kwargs):
        """Add min value validation."""
        defaults = {'min_value': 0}
        defaults.update(kwargs)
        return super(PositiveDecimalField, self).formfield(**defaults)
