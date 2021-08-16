from pydantic import BaseSettings

class Settings(BaseSettings):
    tx_app_token: str
    db_name: str
    db_user: str
    db_password: str
    db_host: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'