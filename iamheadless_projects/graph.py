import networkx as nx

from .conf import settings


DEFAULT_PARENT_ID_ATTRIBUTE = settings.TENANT_MODEL_PARENT_ID_ATTRIBUTE


def get_tenants_graph(model, parent_id_attribute=DEFAULT_PARENT_ID_ATTRIBUTE):
    G = nx.DiGraph()

    for tenant in model.objects.all():

        parent_id = getattr(tenant, parent_id_attribute, None)

        parent_node = None
        tenant_node = tenant.id

        if parent_id is not None:
            parent_node = parent_id

        if parent_node is not None:
            G.add_edge(parent_node, tenant_node)

    return G


def get_tenant_decendants(model, tenant_id, parent_id_attribute=DEFAULT_PARENT_ID_ATTRIBUTE):
    G = get_tenants_graph(model, parent_id_attribute)
    try:
        x = list(G.decendants(tenant_id))
    except nx.exception.NetworkXError:
        return []
    return x


def get_tenant_successors(model, tenant_id, parent_id_attribute=DEFAULT_PARENT_ID_ATTRIBUTE):
    G = get_tenants_graph(model, parent_id_attribute)
    try:
        x = list(G.successors(tenant_id))
    except nx.exception.NetworkXError:
        return []
    return x


def get_tenant_first_successors(model, tenant_id, parent_id_attribute=DEFAULT_PARENT_ID_ATTRIBUTE):
    x = get_tenant_successors(model, tenant_id, parent_id_attribute)
    return next(iter(x), None)
