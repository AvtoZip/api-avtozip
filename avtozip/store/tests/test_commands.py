"""Module to test management commands."""

import os
import shutil
from io import StringIO

from django.conf import settings
from django.core.management import call_command
from django.test import TestCase


class MakeCheckTestCase(TestCase):
    """Class to test `checkmesages` and `makemessages`."""

    @classmethod
    def setUpTestData(cls):  # NOQA
        """sdfsfs."""
        super(MakeCheckTestCase, cls).setUpTestData()
        settings.LOCALE_PATHS = (
            os.path.join(settings.BASE_DIR, 'test_locale'),
        )

    @classmethod
    def tearDownClass(cls):  # NOQA
        """sdfsf."""
        super(MakeCheckTestCase, cls).tearDownClass()
        shutil.rmtree(os.path.join(settings.BASE_DIR, 'test_locale'), ignore_errors=True)

    def setUp(self):  # NOQA
        super(MakeCheckTestCase, self).setUp()
        shutil.rmtree(os.path.join(settings.BASE_DIR, 'test_locale'), ignore_errors=True)

    def test_success_copied(self):
        """Test successful check."""
        out = StringIO()

        shutil.copytree(os.path.join(settings.BASE_DIR, 'locales'), os.path.join(settings.BASE_DIR, 'test_locale'))
        call_command('checkmessages', *'--verbosity 0'.split(), stdout=out)

    def test_not_created(self):
        """Test successful check2."""
        out = StringIO()
        with self.assertRaises(SystemExit) as cm:
            call_command('checkmessages', *'--verbosity 0'.split(), stdout=out)
        self.assertEqual(cm.exception.code, 1)
        self.assertIn('Locale folder does not exist', out.getvalue())

    def test_no_keywords(self):
        """Test w/o makemessages keywords."""
        out = StringIO()
        settings.DEFAULT_EXTRA_KEYWORDS = []
        call_command('makemessages', *'--locale en --locale ru --verbosity 0 --ignore env'.split(), stdout=out)
        with self.assertRaises(SystemExit) as cm:
            call_command('checkmessages', *'--verbosity 3'.split(), stdout=out)
        self.assertEqual(cm.exception.code, 1)
        self.assertIn('You have untranslated messages!', out.getvalue())

    def test_failure_quite(self):
        """Test failed check quite."""
        out = StringIO()
        call_command('makemessages', *'--locale en --locale ru --verbosity 0 --ignore env'.split(), stdout=out)
        with self.assertRaises(SystemExit) as cm:
            call_command('checkmessages', *'--verbosity 0'.split(), stdout=out)
        self.assertEqual(cm.exception.code, 1)
        self.assertEqual('', out.getvalue())

    def test_failure_verbose_1(self):
        """Test failed check verbose."""
        out = StringIO()
        call_command('makemessages', *'--locale en --locale ru --verbosity 0 --ignore env'.split(), stdout=out)
        with self.assertRaises(SystemExit) as cm:
            call_command('checkmessages', *'--verbosity 1'.split(), stdout=out)
        self.assertEqual(cm.exception.code, 1)
        self.assertIn('You have untranslated messages!', out.getvalue())

    def test_failure_verbose_2(self):
        """Test failed check verbose."""
        out = StringIO()
        call_command('makemessages', *'--locale en --locale ru --verbosity 0 --ignore env'.split(), stdout=out)
        with self.assertRaises(SystemExit) as cm:
            call_command('checkmessages', *'--verbosity 2'.split(), stdout=out)
        self.assertEqual(cm.exception.code, 1)
        self.assertIn('You have untranslated messages!', out.getvalue())

    def test_failure_verbose_3(self):
        """Test failed check verbose 3."""
        out = StringIO()
        call_command('makemessages', *'--locale en --locale ru --verbosity 0 --ignore env'.split(), stdout=out)
        with self.assertRaises(SystemExit) as cm:
            call_command('checkmessages', *'--verbosity 3'.split(), stdout=out)
        self.assertEqual(cm.exception.code, 1)
        self.assertIn('You have untranslated messages!', out.getvalue())
