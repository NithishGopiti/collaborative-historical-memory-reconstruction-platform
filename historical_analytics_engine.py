import pandas as pd
from sqlalchemy import text

from historical_database_connection import historical_engine
from historical_query_engine import TOP_EVENT_QUERY

def generate_historical_analytics():

    with historical_engine.connect() as connection:

        result = connection.execute(
            text(TOP_EVENT_QUERY)
        )

        dataframe = pd.DataFrame(
            result.fetchall(),
            columns=result.keys()
        )

        dataframe.to_csv(
            "historical_event_analytics.csv",
            index=False
        )
