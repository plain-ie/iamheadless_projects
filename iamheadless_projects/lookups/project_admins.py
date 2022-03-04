import math

from .. import utils
from .pagination import ALLOWED_FORMATS, pagination


def get_project_admins(
        project_id,
        active=None,
        count='__all__',
        emails=None,
        format='queryset',
        page=1,
        user_ids=None,
        ):

    # --

    User = utils.get_user_model()

    # Normalize and validate

    if format not in ALLOWED_FORMATS:
        raise ValueError('Format not allowed')

    if isinstance(user_ids, list) is False and user_ids is not None:
        user_ids = [user_ids, ]

    if isinstance(emails, list) is False and emails is not None:
        emails = [emails, ]

    if isinstance(active, bool) is False and active is not None:
        raise TypeError('"active" must be bool or None')

    # --

    queryset = User.objects.filter(
        projects__project_id=project_id
    ).prefetch_related(
        'projects'
    )

    if isinstance(user_ids, list) is True:
        if len(user_ids) != 0:
            queryset = queryset.filter(id__in=user_ids)

    if active in [True, False]:
        queryset = queryset.filter(active=active)

    if isinstance(emails, list) is True:
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
