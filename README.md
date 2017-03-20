# Restrict admin django cms

django-adminrestrict-CDSP enables you to block access for django 1.8 or more (work with django CMS) unless requests come from specific IP addresses.

#Installation

`pip install django-adminrestrict-CDSP`

#Configuration

Add the apps to ``settings.py``::

    INSTALLED_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',
        ...
        'restrictadmindjango',
        ...
    )

Next, install the ``FailedLoginMiddleware`` middleware::

    MIDDLEWARE_CLASSES = (
        'restrict_admin_django_cms.middleware.RestrictAdminDjangoCMSMiddleware'
    )

Add in your settings.py :
    If you are using Django CMS, you can use `CMS_INTERNAL_IPS = [...]`
    If you are using only Django, you have to use `ALLOWED_ADMIN_IPS  = [...]`
