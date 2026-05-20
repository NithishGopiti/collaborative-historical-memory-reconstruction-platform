relationship_store = {}

def add_relationship(source, target):

    if source not in relationship_store:
        relationship_store[source] = []

    relationship_store[source].append(target)

def fetch_relationships(source):

    return relationship_store.get(source, [])
