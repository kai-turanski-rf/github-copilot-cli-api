import uuid

from app.cli_connect import get_copilot_completion_without_capturing_input
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    database_url: str = None

    print("Running Copilot CLI test prompt to ensure you are authenticated...")
    test_output: str = get_copilot_completion_without_capturing_input(
        "Hi! This is a test prompt to ensure that the Copilot CLI is working correctly.", uuid.uuid4())
    print("Test output:\n", test_output)
    print("\nGitHub Copilot CLI authentication test complete.")


settings = Settings()
