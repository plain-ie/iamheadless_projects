from ..pydantic_models import UserSchema
from .. import utils
from .pagination import ALLOWED_FORMATS


def get_user(email, format='queryset'):

    User = utils.get_user_model()

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return None

    # --

    if format not in ALLOWED_FORMATS:
        raise ValueError('Format not allowed')

    # --

    if format in ['dict', 'json']:

        pydantic_model = UserSchema.from_django(user)

        if format == 'dict':
            return pydantic_model.dict()

        return pydantic_model.json()

    return user


def change_user_password(email, password, format='queryset'):

    User = utils.get_user_model()

    user = get_user(email)
    if user is None:
        raise User.DoesNotExist()

    # --

    if format not in ALLOWED_FORMATS:
        raise ValueError('Format not allowed')

    if password is not None:
        password = password.strip()
        if len(password) == 0:
            password = None

    # --

    if password is not None:
        user.set_password(password)
        user.save()

    # --

    if format in ['dict', 'json']:

        pydantic_model = UserSchema.from_django(user)

        if format == 'dict':
            return pydantic_model.dict()

        return pydantic_model.json()

    return user


def change_user_name(email, first_name=None, last_name=None, format='queryset'):

    User = utils.get_user_model()

    changed = False

    user = get_user(email)
    if user is None:
        raise User.DoesNotExist()

    # --

    if format not in ALLOWED_FORMATS:
        raise ValueError('Format not allowed')

    # --

    if first_name is not None:
        first_name = first_name.strip()
        if first_name == '':
            first_name = None

    if last_name is not None:
        last_name = last_name.strip()
        if last_name == '':
            last_name = None

    # --

    if first_name is not None:
        user.first_name = first_name
        changed = True

    if last_name is not None:
        user.last_name = last_name
        changed = True

    if changed is True:
        user.save()

    if format in ['dict', 'json']:

        pydantic_model = UserSchema.from_django(user)

        if format == 'dict':
            return pydantic_model.dict()

        return pydantic_model.json()

    return user
