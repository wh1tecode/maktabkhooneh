from myproject.settings import *
from pathlib import Path
from os.path import join



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-xj$o!zg@)vs2k1#c80y%%(e=1b^%i2d5rw3vv$m$jmcl#@67&f"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["online-khosro.com", "www.online-khosro.com"]


MEDIA_URL = "/media/"

STATIC_ROOT = join(BASE_DIR, "static")

MEDIA_ROOT = join(BASE_DIR, "media")


# site
SITE_ID = 2

# robots
ROBOTS_USE_HOST = False
ROBOTS_USE_SITEMAP = False


INTERNAL_IPS = [
    "49.12.48.54",
]



# smtp 
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
# EMAIL_FROM = "kickfundingapp@gmail.com"
EMAIL_HOST_USER = "jojojumung@gmail.com"
EMAIL_HOST_PASSWORD = "qiuk ghdd fbge infe"
EMAIL_PORT = 587
EMAIL_USE_TLS = True

# coming soon
MAINTENANCE_MODE = True