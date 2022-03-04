from djantic import ModelSchema
from pydantic import BaseModel


from . import utils


class UserSchema(ModelSchema):
    class Config:
        model = utils.get_user_model()


class ProjectSchema(ModelSchema):
    class Config:
        model = utils.get_project_model()


class TenantSchema(ModelSchema):
    class Config:
        model = utils.get_tenant_model()


class ProjectAdminSchema(ModelSchema):
    class Config:
        model = utils.get_projectadmin_model()


class TenantUserSchema(ModelSchema):
    class Config:
        model = utils.get_tenantuser_model()


class TenancySchema(ModelSchema):
    class Config:
        model = utils.get_tenancy_model()
