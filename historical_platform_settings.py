from dotenv import load_dotenv
import os

load_dotenv("historical_environment.env")

class HistoricalPlatformSettings:

    MYSQL_HOST = os.getenv("MYSQL_HOST")
    MYSQL_PORT = os.getenv("MYSQL_PORT")
    MYSQL_DATABASE = os.getenv("MYSQL_DATABASE")

    MYSQL_USER = os.getenv("MYSQL_USER")
    MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

    REDIS_HOST = os.getenv("REDIS_HOST")
    REDIS_PORT = os.getenv("REDIS_PORT")

    API_PORT = int(os.getenv("API_PORT", 8040))

platform_settings = HistoricalPlatformSettings()
