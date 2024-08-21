from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    APP_NAME: str
    APP_VERSION: str


    FILE_ALLOWED_TYPES: list
    FILE_MAX_SIZE: int
    FILE_DEFAULT_CHUNK_SIZE: int = 1024 * 1024

    FIREBASE_CREDENTIALS_PATH: str

    class Config:
        env_file = ".env"

def get_settings():
    return Settings()