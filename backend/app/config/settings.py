from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str
    app_version: str
    debug: bool

    log_level: str

    upload_dir: str

    max_file_size: int

    openai_api_key: str = ""

    gemini_api_key: str = ""

    chroma_db_path: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore"
    )


settings = Settings()