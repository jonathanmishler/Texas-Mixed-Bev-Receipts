from pydantic import BaseSettings

class Settings(BaseSettings):
    tx_app_token: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'