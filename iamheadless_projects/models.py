from django.core.cache import cache
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import PermissionDenied, ValidationError
from django.db import models

from .conf import settings
from . import managers


class User(AbstractUser):

    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = managers.CustomUserManager()

    def save(self, *args, **kwargs):
        creation = getattr(self, 'id', None) is None
        if self.email in [None, '', ' ']:
            raise ValidationError('Email is required')
        self.email = self.email.lower()
        self.username = self.email
        super(User, self).save(*args, **kwargs)


class Project(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class Tenant(models.Model):
    name = models.CharField(max_length=255, blank=True, null=True)
    parent = models.ForeignKey('Tenant', related_name='children', on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.name


class ProjectAdmin(models.Model):

    class Meta:
        unique_together = ('project', 'user')

    project = models.ForeignKey('Project', related_name='users', on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name='projects', on_delete=models.CASCADE)
    acl = models.CharField(max_length=255, blank=True, null=True)


class TenantUser(models.Model):

    class Meta:
        unique_together = ('tenant', 'user')

    tenant = models.ForeignKey('Tenant', related_name='users', on_delete=models.CASCADE)
    user = models.ForeignKey('User', related_name='tenants', on_delete=models.CASCADE)
    acl = models.CharField(max_length=255, blank=True, null=True)


class Tenancy(models.Model):

    class Meta:
        unique_together = ('project', 'tenant')

    project = models.ForeignKey('Project', related_name='tenants', on_delete=models.CASCADE)
    tenant = models.ForeignKey('Tenant', related_name='projects', on_delete=models.CASCADE)
