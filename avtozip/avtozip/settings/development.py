"""Django development settings to override production."""

from ..utils import inject_settings


# Default values for overriden settings
INSTALLED_APPS = []

# Inject default settings to avoid wildcard import
inject_settings('avtozip.settings.production', locals())

# Debug settings
DEBUG = True
ALLOWED_HOSTS = []

# Django TastyPie settings
TASTYPIE_DEFAULT_FORMATS = ['json']

# Additional applications
INSTALLED_APPS += [
    'debug_toolbar',
    'rosetta',
]

# Proxy settings
PROXY_TECDOC_URL = 'http://localhost:8013/api/tecdoc_v1'
