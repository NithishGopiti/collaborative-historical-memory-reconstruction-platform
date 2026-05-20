from historical_database_connection import historical_engine
from historical_models import Base

def initialize_tables():
    Base.metadata.create_all(bind=historical_engine)

if __name__ == "__main__":
    initialize_tables()
