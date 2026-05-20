def validate_event_structure(event):

    required_fields = [
        "title",
        "description",
        "event_year"
    ]

    for field in required_fields:

        if field not in event:
            return False

    if len(event["description"]) < 50:
        return False

    return True
