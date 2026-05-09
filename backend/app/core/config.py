from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file='.env', env_file_encoding='utf-8', extra='ignore')

    app_name: str = 'Ransomware Resilience Platform'
    environment: str = 'dev'
    api_prefix: str = '/api/v1'

    secret_key: str = 'change-me'
    access_token_expire_minutes: int = 60
    algorithm: str = 'HS256'

    postgres_dsn: str = 'postgresql+asyncpg://postgres:postgres@postgres:5432/resilience'
    redis_url: str = 'redis://redis:6379/0'

    encryption_key: str = 'bXlzdXBlcnNlY3JldGtleW15c3VwZXJzZWNyZXRrZXk='


settings = Settings()
