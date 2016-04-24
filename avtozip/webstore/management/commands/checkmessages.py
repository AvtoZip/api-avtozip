"""Command to find untranslated entries in PO files."""

import os
import sys
from collections import defaultdict

from django.conf import settings
from django.core.management.base import BaseCommand

import polib


class Command(BaseCommand):
    """Checkmessages command implementation."""

    help = 'Check for untranslated messages in all installed languages'

    def add_arguments(self, parser):
        """Add extra keywords to the command."""
        super(Command, self).add_arguments(parser)
        parser.add_argument(
            '-s', '--skip-locale', dest='skip_locales', action='append', default=settings.DEFAULT_SKIPPED_LOCALES,
            help='Skip check for locales (default: "EN")',
        )

    def handle(self, *args, **options):
        """Process all locales defined in settings and find untranslated entries."""
        results = defaultdict(list)
        for language_code, _ in settings.LANGUAGES:
            if language_code in options['skip_locales']:
                if options['verbosity'] > 1:
                    self.stdout.write('Skipping locale "{}"'.format(language_code.upper()))
                continue
            for location in settings.LOCALE_PATHS:
                filepath = '{0}/{1}/LC_MESSAGES/django.po'.format(location, language_code)
                if os.path.isfile(filepath):
                    untranslated = polib.pofile(filepath).untranslated_entries()
                    for entry in untranslated:
                        results[filepath].append('{1} # {0}'.format(entry.msgid, entry.linenum))
                else:
                    self.stdout.write('Locale folder does not exist: {0}'.format(filepath))
                    sys.exit(1)
        if results:
            if options['verbosity'] > 0:
                self.stdout.write('You have untranslated messages!')
                for code, values in results.items():
                    if options['verbosity'] > 1:
                        self.stdout.write('{0}File {1}:'.format(' ' * 2, code))
                        if options['verbosity'] > 2:
                            for value in values:
                                self.stdout.write('{0}{1}'.format(' ' * 4, value))
            sys.exit(1)
