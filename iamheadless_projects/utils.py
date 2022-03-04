from django.apps import apps
from django.conf import settings as dj_settings
from django.contrib.auth import get_user_model as dj_get_user_model

from .conf import settings
from .loader import get_model


def get_user_model(format='class'):
    if format == 'string':
        return dj_settings.AUTH_USER_MODEL
    return dj_get_user_model()


def get_project_model(format='class'):
    string = settings.PROJECT_MODEL_CLASS
    if format == 'string':
        return string
    return get_model(string, format)


def get_projectadmin_model(format='class'):
    string = settings.PROJECTADMIN_MODEL_CLASS
    if format == 'string':
        return string
    return get_model(string, format)


def get_tenant_model(format='class'):
    string = settings.TENANT_MODEL_CLASS
    if format == 'string':
        return string
    return get_model(string, format)


def get_tenancy_model(format='class'):
    string = settings.TENANCY_MODEL_CLASS
    if format == 'string':
        return string
    return get_model(string, format)


def get_tenantuser_model(format='class'):
    string = settings.TENANTUSER_MODEL_CLASS
    if format == 'string':
        return string
    return get_model(string, format)
