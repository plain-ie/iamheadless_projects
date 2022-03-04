from .. import utils
from ..pydantic_models import TenantSchema
from .pagination import ALLOWED_FORMATS


def get_tenant(
        tenant_id,
        project_id=None,
        format='queryset'
        ):

    # --

    Tenant = utils.get_tenant_model()

    # --

    if format not in ALLOWED_FORMATS:
        raise ValueError('Format not allowed')

    if isinstance(tenant_id, str) is False:
        tenant_id = str(tenant_id)

    if project_id is not None:
        if isinstance(project_id, str) is False:
            project_id = str(project_id)

    # --

    try:
        if project_id is None:
            tenant = Tenant.objects.get(id=tenant_id)
        else:
            tenant = Tenant.objects.get(
                id=tenant_id,
                projects__project_id=project_id
            )
    except Tenant.DoesNotExist:
        return None

    # --

    if format in ['dict', 'json']:

        pydantic_model = TenantSchema.form_django(tenant)

        if format == 'dict':
            return pydantic_model.dict()

        return pydantic_model.json()

    return tenant
