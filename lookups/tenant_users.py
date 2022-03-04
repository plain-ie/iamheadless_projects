import math

from django.db.models import Q

from .. import utils
from ..conf import settings
from ..graph import get_tenant_successors
from ..pydantic_models import UserSchema
from .pagination import ALLOWED_FORMATS, pagination


def get_tenant_users(
        tenant_id,
        active=None,
        count='__all__',
        emails=None,
        format='queryset',
        page=1,
        user_ids=None,
        ):

    # --

    User = utils.get_user_model()
    Tenant = utils.get_tenant_model()

    # --

    if format not in ALLOWED_FORMATS:
        raise ValueError('Format not allowed')

    if isinstance(user_ids, list) is False and user_ids is not None:
        user_ids = [user_ids, ]

    if isinstance(emails, list) is False and emails is not None:
        emails = [emails, ]

    if isinstance(active, bool) is False and active is not None:
        raise TypeError('"active" must be bool or None')

    # --

    successors = get_tenant_successors(
        Tenant,
        tenant_id,
        settings.TENANT_MODEL_PARENT_ID_ATTRIBUTE
    )

    ids = successors + [tenant_id]

    # --

    condition = Q()
    condition.add(Q(tenants__tenant_id__in=ids), Q.OR)
    condition.add(Q(projects__project__tenants__tenant_id__in=ids), Q.OR)

    queryset = User.objects.filter(
        condition
    ).prefetch_related(
        'tenants',
        'projects__project__tenants'
    )

    if isinstance(user_ids, list) is True:
        if len(user_ids) != 0:
            queryset = queryset.filter(id__in=user_ids)

    if active in [True, False]:
        queryset = queryset.filter(active=active)

    if isinstance(emails, list) is True:
        emails_length = len(emails)
        if emails_length == 1:
            queryset = queryset.filter(email=emails[0])
        if emails_length > 1:
            queryset = queryset.filter(email__in=emails)

    # --

    paginated_data = pagination(queryset, page, count, UserSchema)

    if format == 'dict':
        return paginated_data.dict

    if format == 'json':
        return paginated_data.json

    return paginated_data
