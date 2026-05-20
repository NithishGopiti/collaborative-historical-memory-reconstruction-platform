from historical_version_controller import version_store

def rollback_event(event_id, version_number):

    versions = version_store.get(event_id, [])

    for version in versions:

        if version["version"] == version_number:
            return version

    return None
