# -*- coding: utf-8 -*-

"""
A sample of kay settings.

:Copyright: (c) 2009 Accense Technology, Inc. 
                     Takashi Matsuo <tmatsuo@candit.jp>,
                     All rights reserved.
:license: BSD, see LICENSE for more details.
"""

DEFAULT_TIMEZONE = 'Asia/Tokyo'
DEBUG = True
PROFILE = False
SECRET_KEY = 'ReplaceItWithSecretString'
SESSION_PREFIX = 'gaesess:'
COOKIE_AGE = 1209600 # 2 weeks
COOKIE_NAME = 'KAY_SESSION'

ADD_APP_PREFIX_TO_KIND = True

ADMINS = (
)

TEMPLATE_DIRS = (
)

USE_I18N = True
DEFAULT_LANG = 'en'

INSTALLED_APPS = (
  'myapp',
)

APP_MOUNT_POINTS = {
  'myapp': '/',
}

# You can remove following settings if unnecessary.
CONTEXT_PROCESSORS = (
  'kay.context_processors.request',
  'kay.context_processors.url_functions',
  'kay.context_processors.media_url',
)

MIDDLEWARE_CLASSES = (
  'kay.auth.middleware.AuthenticationMiddleware',
  'kay.utils.flash.FlashMiddleware',
)

AUTH_USER_MODEL = 'myapp.models.MyUser'

USE_DB_HOOK = True
