import math

from .. import utils
from .. pydantic_models import TenantSchema
from .pagination import ALLOWED_FORMATS, pagination


def get_project_tenants(
        project_id,
        count='__all__',
        format='queryset',
        page=1,
        q=None,
        tenant_ids=None,
        ):

    # --

    Tenant = utils.get_tenant_model()

    # --

    if format not in ALLOWED_FORMATS:
        raise ValueError('Format not allowed')

    if isinstance(tenant_ids, list) is False and tenant_ids is not None:
        tenant_ids = [tenant_ids, ]

    # --

    queryset = Tenant.objects.filter(
        projects__project_id=project_id
    ).prefetch_related(
        'projects'
    )

    if isinstance(tenant_ids, list) is True:
        if len(tenant_ids) != 0:
            queryset = queryset.filter(id__in=tenant_ids)

    # --

    paginated_data = pagination(queryset, page, count, TenantSchema)

    if format == 'dict':
        return paginated_data.dict

    if format == 'json':
        return paginated_data.json

    return paginated_data
