from pydantic import BaseSettings
import os

class Settings(BaseSettings):
    log_level: str = 'DEBUG'
    service_id: str = os.getenv('SERVICE_ID')
    version: str = os.getenv('VERSION')
    release_id: str = os.getenv('RELEASE_ID')
    environment: str = os.getenv('ENVIRONMENT')


settings = Settings()
