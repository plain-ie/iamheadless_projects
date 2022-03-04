from .. import utils


def get_user_permissions(
        user_id,
        project_ids=None,
        ):

    cleaned_list = None
    data = dict()

    if isinstance(project_ids, list) is False and project_ids is not None:
        project_ids = [project_ids, ]

    if isinstance(project_ids, list) is True:
        cleaned_list = []
        for x in project_ids:
            if isinstance(x, str) is False:
                x = str(x)
            cleaned_list.append(x)

    ProjectAdmin = utils.get_projectadmin_model()
    Tenant = utils.get_tenant_model()

    queryset = ProjectAdmin.objects.filter(user_id=user_id)

    if cleaned_list is not None:
        queryset = queryset.filter(project_id__in=cleaned_list)

    for x in queryset:
        data[str(x.project_id)] = '*'

    admin_project_ids = data.keys()
    non_admin_project_ids = list(set(project_ids) - set(admin_project_ids))

    if len(non_admin_project_ids) == 0:
        return data

    # XXXX TODO: Requires optimizations ASAP
    for x in non_admin_project_ids:

        if x not in data:
            data[x] = {}

        queryset = Tenant.objects.filter(
            projects__tenant__users__user_id=user_id,
            projects__project_id=x,
        ).values_list('id', flat=True)

        for y in queryset:
            data[x][str(y)] = '*'

        if data[x] == {}:
            data.pop(x)

    return data
