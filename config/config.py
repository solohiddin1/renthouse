from pydantic_settings import BaseSettings
from pydantic import Field
from dotenv import load_dotenv
import os

# from house.settings import BASE_DIR

# load_dotenv(os.path.join(BASE_DIR, 'config','.env'))
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

class Settings(BaseSettings):
    PHOTO_PATH: str
    DEFAULT_PHOTO_PATH: str
    
    # db
    DATABASE_PASSWORD: str
    DATABASE_NAME: str
    DATABASE_USER: str
    DATABASE_HOST: str
    DATABASE_PORT: str
    DATABASE_ENGINE: str
    # django
    SECRET_KEY: str
    DEBUG: str

    ALLOWED_HOSTS: str
    # ALLOWED_HOSTS: list[str] = Field(default_factory=list)
    
    # email
    EMAIL_HOST: str
    EMAIL_PORT: int
    EMAIL_HOST_USER: str
    EMAIL_HOST_PASSWORD: str
    EMAIL_USE_TLS: bool
    DEFAULT_FROM_EMAIL: str
    SERVER_EMAIL: str
    EMAIL_BACKEND: str
    
    # some
    TIME_ZONE: str
    LANGUAGE_CODE: str

    class Config:
        env_file = ".env"
        # env_file = os.path.join(BASE_DIR,'config', '.env')
        env_file_encoding = "utf-8"
    

settings = Settings()