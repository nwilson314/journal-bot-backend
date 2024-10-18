from typing import Generator

from .openai import OpenAIClient, get_openai_client


def yield_ai_client() -> Generator[OpenAIClient, None, None]:
    yield get_openai_client()
