import math

from django.db.models import Q

from .. import utils
from ..conf import settings
from ..pydantic_models import UserSchema
from .pagination import ALLOWED_FORMATS, pagination


def get_users(
        active=None,
        count='__all__',
        emails=None,
        format='queryset',
        page=1,
        ):

    # --

    User = utils.get_user_model()

    # --

    if format not in ALLOWED_FORMATS:
        raise ValueError('"format" is not allowed')

    if isinstance(emails, list) is False and emails is not None:
        emails = [emails, ]

    if isinstance(active, bool) is False and active is not None:
        raise TypeError('"active" must be bool or None')

    if isinstance(page, int) is False:
        raise TypeError('"page" must be int')

    # --

    queryset = User.objects.all()

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
