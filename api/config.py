from pathlib import Path

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    host: str
    port: int

    project_name: str = "test_task"
    version: str = "0.0.1"
    description: str = "Test task"


settings = Settings(_env_file=Path(__file__).parent.parent / ".env")
