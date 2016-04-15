"""Custom makemessages command to support additional keywords."""

from django.conf import settings
from django.core.management.commands import makemessages


class Command(makemessages.Command):
    """Custom makemessages command implementation."""

    def add_arguments(self, parser):
        """Add extra keywords to the command."""
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '--extra-keyword', dest='xgettext_keywords', action='append', default=settings.DEFAULT_EXTRA_KEYWORDS,
        )

    def handle(self, *args, **options):
        """Handle command and process extra arguments."""
        xgettext_keywords = options.pop('xgettext_keywords')
        if xgettext_keywords:
            self.xgettext_options = (
                makemessages.Command.xgettext_options[:] + ['--keyword={0}'.format(kwd) for kwd in xgettext_keywords]
            )
        super(Command, self).handle(*args, **options)
