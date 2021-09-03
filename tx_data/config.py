from pydantic import BaseSettings

class Settings(BaseSettings):
    """ Settings for the Texas Open Data API """
    tx_app_token: str

    class Config:
        env_file = '.env'
        env_file_encoding = 'utf-8'