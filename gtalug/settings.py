# Django settings for pygta project.
import os.path

ROOT_PATH = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	# ('Your Name', 'your_email@domain.com'),
	('Myles Braithwaite', 'me+gtalug@mylesbraithwaite.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = ''			# 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
DATABASE_NAME = ''				# Or path to database file if using sqlite3.
DATABASE_USER = ''				# Not used with sqlite3.
DATABASE_PASSWORD = ''			# Not used with sqlite3.
DATABASE_HOST = ''				# Set to empty string for localhost. Not used with sqlite3.
DATABASE_PORT = ''				# Set to empty string for default. Not used with sqlite3.

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# If running in a Windows environment this must be set to the same as your
# system time zone.
TIME_ZONE = 'America/Toronto'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-ca'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(ROOT_PATH, 'media')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/media/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = '/media/admin/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '+u!y)^cz3sc-kj5q3mk6q(p*83^r=bys*c2_ok*4%9qy)_!wpn'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
	'django.template.loaders.filesystem.load_template_source',
	'django.template.loaders.app_directories.load_template_source',
	# 'django.template.loaders.eggs.load_template_source',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	"django.core.context_processors.auth",
	"django.core.context_processors.debug",
	"django.core.context_processors.i18n",
	"django.core.context_processors.media",
	"django.core.context_processors.request"
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'gtalug.urls'

TEMPLATE_DIRS = (
	# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
	# Always use forward slashes, even on Windows.
	# Don't forget to use absolute paths, not relative paths.
	os.path.join(ROOT_PATH, 'templates'),
)

SHORTEN_MODELS = {
	'P': 'flatpages.flatpage',
	'B': 'blog.post',
	'M': 'meetings.meeting',
	'E': 'events.event',
}

SHORT_BASE_URL = SHORTEN_FULL_BASE_URL = 'http://gtalug.org/'

HAYSTACK_SITECONF = 'gtalug.apps.search'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(ROOT_PATH, '../haystack/')

from gtalug.settings_local import *

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.admin',
	'django.contrib.admindocs',
	'django.contrib.flatpages',
	'django.contrib.sitemaps',
	'django.contrib.comments',
	
	'shorturls',
	'django_extensions',
	'haystack',
	'south',
	'perfect404',
	'piston',
		
	'gtalug.apps.meetings',
	'gtalug.apps.blog',
	'gtalug.apps.events',
	'gtalug.apps.planet',
	'gtalug.apps.search',
	'gtalug.apps.utils',
	'gtalug.apps.api',
)

DATE_FORMAT = 'jS F, Y'
TIME_FORMAT = 'f a'
DATETIME_FORMAT = DATE_FORMAT + " " + TIME_FORMAT