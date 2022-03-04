from django.conf import settings as dj_settings

from .apps import IamheadlessProjectsConfig


class Settings:

    APP_NAME = IamheadlessProjectsConfig.name
    VAR_PREFIX = APP_NAME.upper()

    VAR_PROJECT_MODEL_CLASS = f'{VAR_PREFIX}_PROJECT_MODEL_CLASS'
    VAR_PROJECTADMIN_MODEL_CLASS = f'{VAR_PREFIX}_PROJECTADMIN_MODEL_CLASS'
    VAR_TENANT_MODEL_CLASS = f'{VAR_PREFIX}_TENANT_MODEL_CLASS'
    VAR_TENANT_MODEL_PARENT_ID_ATTRIBUTE = f'{VAR_PREFIX}_TENANT_MODEL_PARENT_ID_ATTRIBUTE'
    VAR_TENANTUSER_MODEL_CLASS = f'{VAR_PREFIX}_TENANTUSER_MODEL_CLASS'
    VAR_TENANCY_MODEL_CLASS = f'{VAR_PREFIX}_TENANCY_MODEL_CLASS'
    VAR_TENANCYUSER_MODEL_CLASS = f'{VAR_PREFIX}_TENANCYUSER_MODEL_CLASS'

    @property
    def PROJECT_MODEL_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_PROJECT_MODEL_CLASS,
            f'{self.APP_NAME}.Project'
        )

    @property
    def PROJECTADMIN_MODEL_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_PROJECTADMIN_MODEL_CLASS,
            f'{self.APP_NAME}.ProjectAdmin'
        )

    @property
    def TENANT_MODEL_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_TENANT_MODEL_CLASS,
            f'{self.APP_NAME}.Tenant'
        )

    @property
    def TENANT_MODEL_PARENT_ID_ATTRIBUTE(self):
        return getattr(
            dj_settings,
            self.VAR_TENANT_MODEL_PARENT_ID_ATTRIBUTE,
            'parent_id'
        )

    @property
    def TENANCY_MODEL_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_TENANCY_MODEL_CLASS,
            f'{self.APP_NAME}.Tenancy'
        )

    @property
    def TENANTUSER_MODEL_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_TENANTUSER_MODEL_CLASS,
            f'{self.APP_NAME}.TenantUser'
        )

    @property
    def TENANCYUSER_MODEL_CLASS(self):
        return getattr(
            dj_settings,
            self.VAR_TENANCYUSER_MODEL_CLASS,
            f'{self.APP_NAME}.TenancyUser'
        )

    def __getattr__(self, name):
        return getattr(dj_settings, name)


settings = Settings()
