TOP_EVENT_QUERY = '''
SELECT
    event_year,
    COUNT(*) AS total_events
FROM historical_events
GROUP BY event_year
ORDER BY total_events DESC
'''
