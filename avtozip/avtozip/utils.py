"""Utilites for general project point."""

from importlib import import_module


def inject_settings(path, context, fail_silently=False):
    """Inject settings from module at path to the given context.

    Do not raise an Import Error when fail silently enabled.
    """
    try:
        module = import_module(path)
    except ImportError:
        if fail_silently:
            return
        raise

    for attr in dir(module):
        if attr[0] == '_' or not attr.isupper():
            continue
        context[attr] = getattr(module, attr)
