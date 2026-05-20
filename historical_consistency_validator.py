def validate_consistency(event_years):

    for year in event_years:

        if year < 0:
            return False

    return True
