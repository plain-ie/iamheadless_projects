from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms.custom_user_forms import CustomUserChangeForm, CustomUserCreationForm
from . import models


class UserAdmin(UserAdmin):

    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = models.User

    list_display = (
        'first_name',
        'last_name',
        'email',
        'is_staff',
        'is_active',
    )

    list_filter = (
        'email',
        'is_staff',
        'is_active',
    )

    fieldsets = (
        (
            None,
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'email',
                    'password'
                )
            }
        ),
        (
            'Permissions',
            {
                'fields': (
                    'is_staff',
                    'is_active',
                    'is_superuser',
                )
            }
        ),
    )

    add_fieldsets = (
        (
            None, {
                'classes': (
                    'wide',
                ),
                'fields': (
                    'email',
                    'password1',
                    'password2',
                    'is_staff',
                    'is_active',
                    'is_superuser',
                )
            }
        ),
    )

    search_fields = (
        'email',
    )

    ordering = (
        'email',
    )


class TenantAdmin(admin.ModelAdmin):
    model = models.Tenant
    raw_id_fields = ['parent']
    list_display = ['name']


class ProjectAdminAdmin(admin.ModelAdmin):
    model = models.ProjectAdmin
    raw_id_fields = ['project', 'user']
    list_display = ['project', 'user']


class TenantUserAdmin(admin.ModelAdmin):
    model = models.TenantUser
    raw_id_fields = ['tenant', 'user']
    list_display = ['tenant', 'user']


class TenancyAdmin(admin.ModelAdmin):
    model = models.Tenancy
    raw_id_fields = ['project', 'tenant']
    list_display = ['project', 'tenant']


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Project)
admin.site.register(models.ProjectAdmin, ProjectAdminAdmin)
admin.site.register(models.Tenancy, TenancyAdmin)
admin.site.register(models.Tenant, TenantAdmin)
admin.site.register(models.TenantUser, TenantUserAdmin)
