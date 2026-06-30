# from pydantic_settings import BaseSettings, SettingsConfigDict


# class Settings(BaseSettings):
#     app_name: str
#     app_version: str
#     debug: bool

#     log_level: str

#     upload_dir: str

#     max_file_size: int

#     openai_api_key: str = ""

#     gemini_api_key: str = ""

#     chroma_db_path: str

#     model_config = SettingsConfigDict(
#         env_file=".env",
#         extra="ignore"
#     )


# settings = Settings()

from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    """

    app_name: str = "AI Recruitment Intelligence"
    app_version: str = "0.1.0"

    debug: bool = True

    log_level: str = "INFO"

    upload_dir: str = "uploads"

    max_file_size: int = 10 * 1024 * 1024

    openai_api_key: str = ""

    gemini_api_key: str = ""

    chroma_db_path: str = "./vector_db"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


@lru_cache
def get_settings() -> Settings:
    """
    Return cached application settings.
    """
    return Settings()


settings = get_settings()