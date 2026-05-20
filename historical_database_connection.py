from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from historical_platform_settings import platform_settings

DATABASE_URL = (
    f"mysql+pymysql://{platform_settings.MYSQL_USER}:"
    f"{platform_settings.MYSQL_PASSWORD}@"
    f"{platform_settings.MYSQL_HOST}:"
    f"{platform_settings.MYSQL_PORT}/"
    f"{platform_settings.MYSQL_DATABASE}"
)

historical_engine = create_engine(
    DATABASE_URL,
    pool_size=30,
    max_overflow=60,
    pool_pre_ping=True,
    pool_recycle=3600
)

HistoricalSession = sessionmaker(
    bind=historical_engine,
    autocommit=False,
    autoflush=False
)
