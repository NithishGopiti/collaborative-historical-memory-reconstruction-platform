from datetime import datetime

version_store = {}

def create_version(event_id, summary):

    if event_id not in version_store:
        version_store[event_id] = []

    version_number = len(
        version_store[event_id]
    ) + 1

    version_store[event_id].append({
        "version": version_number,
        "summary": summary,
        "timestamp": datetime.utcnow().isoformat()
    })

    return version_number
