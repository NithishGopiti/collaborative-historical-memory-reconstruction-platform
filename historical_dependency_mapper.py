import networkx as nx

dependency_graph = nx.DiGraph()

def add_dependency(source_event, dependent_event):

    dependency_graph.add_edge(
        source_event,
        dependent_event
    )

def validate_circular_dependency():

    return nx.is_directed_acyclic_graph(
        dependency_graph
    )
