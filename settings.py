# Initialize App Engine and import the default settings (DB backend, etc.).
# If you want to use a different backend you have to remove all occurences
# of "djangoappengine" from this file.
from djangoappengine.settings_base import *
import os

# little helpers
SITE_ROOT = os.path.dirname(os.path.realpath(__file__))
rel = lambda p: os.path.join(SITE_ROOT, p)

# Activate django-dbindexer for the default database
DATABASES['native'] = DATABASES['default']
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': 'native'}
AUTOLOAD_SITECONF = 'indexes'

INSTALLED_APPS = (
#    'django.contrib.admin',
	'django.contrib.contenttypes',
	'django.contrib.auth',
	'django.contrib.sessions',
	'django.contrib.staticfiles',
	'django.contrib.messages',
	'djangotoolbox',
	'autoload',
	'dbindexer',
	'blog',
	'social_auth',
	'registration',


	# djangoappengine should come last, so it can override a few manage.py commands
	'djangoappengine',
)

MIDDLEWARE_CLASSES = (
	# This loads the index definitions, so it has to come first
	'autoload.middleware.AutoloadMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'social_auth.middleware.SocialAuthExceptionMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.contrib.auth.context_processors.auth',
	'django.core.context_processors.request',
	'django.core.context_processors.media',
	"django.core.context_processors.static",
	'django.contrib.messages.context_processors.messages',
	'social_auth.context_processors.social_auth_by_name_backends',
	'social_auth.context_processors.social_auth_backends',
	'social_auth.context_processors.social_auth_login_redirect',
)

# This test runner captures stdout and associates tracebacks with their
# corresponding output. Helps a lot with print-debugging.
TEST_RUNNER = 'djangotoolbox.test.CapturingTestSuiteRunner'

ADMIN_MEDIA_PREFIX = '/media/admin/'
TEMPLATE_DIRS = (os.path.join(os.path.dirname(__file__), 'templates'),)

ROOT_URLCONF = 'urls'
APPEND_SLASH = True

# all static files are served from static dir
STATICFILES_FINDERS = (
	'django.contrib.staticfiles.finders.FileSystemFinder',
	'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

STATIC_URL = '/static/'
STATICFILES_DIRS = (
	rel('static'),
)


# social auth stuff
AUTHENTICATION_BACKENDS = (
	'django.contrib.auth.backends.ModelBackend',
	'social_auth.backends.facebook.FacebookBackend',
	'social_auth.backends.contrib.github.GithubBackend',
	'social_auth.backends.google.GoogleBackend',
	'social_auth.backends.twitter.TwitterBackend',
)


LOGIN_URL = '/account/login/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL = '/login/error'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/admin/'
SOCIAL_AUTH_NEW_ASSOCIATION_REDIRECT_URL = '/account/association/'
SOCIAL_AUTH_DISCONNECT_REDIRECT_URL = '/account/disconnection/'

ACCOUNT_ACTIVATION_DAYS = 7

import random
SOCIAL_AUTH_DEFAULT_USERNAME = lambda: random.choice(['Darth Vader', 'Obi-Wan Kenobi', 'R2-D2', 'C-3PO', 'Yoda'])
SOCIAL_AUTH_UUID_LENGTH = 16

try:
	from sensitive_settings import *
except ImportError:
	import sys
	print >>sys.stderr, 'Could not import from sensitive_settings, social login will not work'

DEBUG = True
