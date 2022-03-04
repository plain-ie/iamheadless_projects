import json
import math

from django.core.serializers import serialize
from django.db.models.query import QuerySet


ALLOWED_FORMATS = [
    'dict',
    'json',
    'queryset'
]


class Pagination:

    def __init__(
            self,
            page=1,
            pages=1,
            queryset=QuerySet(),
            total=0,
            pydantic_model=None,
            ):

        self.page = page
        self.pages = pages
        self.queryset = queryset
        self.total = total
        self.pydantic_model = pydantic_model

    @property
    def data(self):
        return {
            'page': self.page,
            'pages': self.pages,
            'results': self.queryset,
            'total': self.total
        }

    @property
    def dict(self):
        data = self.data
        results = data['results']
        if self.pydantic_model is None:
            data['results'] = self.queryset_to_dict(results)
        else:
            _results = []
            for x in self.pydantic_model.from_django(results, many=True):
                _results.append(x.dict())
            data['results'] = _results
        return data

    @property
    def json(self):
        return json.dumps(self.dict)

    def queryset_to_dict(self, queryset):

        data = serialize(
            'json',
            queryset
        )

        data = json.loads(data)

        _d = []

        for x in data:
            id = x.pop('pk')
            field_data = x.pop('fields')
            field_data['id'] = id
            _d.append(field_data)

        return _d


def pagination(queryset, page, count, pydantic_model=None):

    if isinstance(queryset, QuerySet) is False:
        raise TypeError('"queryset" must be Queryset')

    if isinstance(page, int) is False:
        raise TypeError('"page" must be int')

    if isinstance(count, int) is False:
        raise TypeError('"count" must be int')

    total = queryset.count()
    pages = 1

    if count != '__all__':
        pages = math.ceil(total/count)
        start_index = (page - 1) * count
        end_index = start_index + count
        queryset = queryset[start_index : end_index]

    return Pagination(
        page=page,
        pages=pages,
        queryset=queryset,
        total=total,
        pydantic_model=pydantic_model
    )
