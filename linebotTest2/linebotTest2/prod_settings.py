from .settings import *
STATIC_ROOT='staticfiles'
SECURE_PROXY_SSL_HEADER=('HTTP_X_FORWARDING_PROTO','https')
ALLOWED_HOSTS=['*']
DEBUG=False