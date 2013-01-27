# -*- coding: utf-8 -*-
from datetime import timedelta

from django.conf import settings
from django.utils.translation import ugettext_lazy as _

AXES_SETTINGS_NAMES = {
    'FAILURE_LIMIT': 'AXES_LOGIN_FAILURE_LIMIT',
    'LOCK_OUT_AT_FAILURE': 'AXES_LOCK_OUT_AT_FAILURE',
    'USE_USER_AGENT': 'AXES_USE_USER_AGENT',
    'BEHIND_REVERSE_PROXY': 'AXES_BEHIND_REVERSE_PROXY',
    'REVERSE_PROXY_HEADER': 'AXES_REVERSE_PROXY_HEADER',
    'COOLOFF_TIME': 'AXES_COOLOFF_TIME',
    'LOGGER': 'AXES_LOGGER',
    'LOCKOUT_TEMPLATE': 'AXES_LOCKOUT_TEMPLATE',
    'VERBOSE': 'AXES_VERBOSE',
    'ONLY_WHITELIST': 'AXES_ONLY_ALLOW_WHITELIST',
    'IP_WHITELIST': 'AXES_IP_WHITELIST',
    'IP_BLACKLIST': 'AXES_IP_BLACKLIST',
    }

# see if the user has overridden the failure limit
FAILURE_LIMIT = getattr(settings, 'AXES_LOGIN_FAILURE_LIMIT', 3)

# see if the user has set axes to lock out logins after failure limit
LOCK_OUT_AT_FAILURE = getattr(settings, 'AXES_LOCK_OUT_AT_FAILURE', True)

USE_USER_AGENT = getattr(settings, 'AXES_USE_USER_AGENT', False)

#see if the django app is sitting behind a reverse proxy
BEHIND_REVERSE_PROXY = getattr(settings, 'AXES_BEHIND_REVERSE_PROXY', False)
#if the django app is behind a reverse proxy, look for the ip address using this HTTP header value
REVERSE_PROXY_HEADER = getattr(settings, 'AXES_REVERSE_PROXY_HEADER', 'HTTP_X_FORWARDED_FOR')


COOLOFF_TIME = getattr(settings, 'AXES_COOLOFF_TIME', None)
if isinstance(COOLOFF_TIME, int):
    COOLOFF_TIME = timedelta(hours=COOLOFF_TIME)

LOGGER = getattr(settings, 'AXES_LOGGER', 'axes.watch_login')

LOCKOUT_TEMPLATE = getattr(settings, 'AXES_LOCKOUT_TEMPLATE', None)
VERBOSE = getattr(settings, 'AXES_VERBOSE', True)

# whitelist and blacklist
# todo: convert the strings to IPv4 on startup to avoid type conversion during processing
ONLY_WHITELIST = getattr(settings, 'AXES_ONLY_ALLOW_WHITELIST', False)
IP_WHITELIST = getattr(settings, 'AXES_IP_WHITELIST', None)
IP_BLACKLIST = getattr(settings, 'AXES_IP_BLACKLIST', None)

ERROR_MESSAGE = _("Please enter a correct username and password. "
                              "Note that both fields are case-sensitive.")
LOGIN_FORM_KEY = 'this_is_the_login_form'

def get_lockout_url():
    return getattr(settings, 'AXES_LOCKOUT_URL', None)

def get_setting(name):
    try:
        from constance import config
    except ImportError:
        return getattr(locals(), name, None)
    return getattr(config, AXES_SETTINGS_NAMES.get(name, name), getattr(locals(), name, None))