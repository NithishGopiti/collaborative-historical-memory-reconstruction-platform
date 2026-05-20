def detect_conflict(existing_year, incoming_year):

    if abs(existing_year - incoming_year) > 500:
        return True

    return False
