from llama_index.core import Settings
from llama_index.core.prompts import PromptTemplate
from llama_index.llms.openai import OpenAI as LlamaOpenAI

from journal_bot.lib.templates import LLAMA_JOURNAL_ANALYZE_TEMPLATE


class OpenAIClient:
    def __init__(
        self,
    ) -> None:
        self.llama_llm = LlamaOpenAI(model="gpt-4o-mini", temperature=0.9)
        Settings.llm = self.llama_llm

    def analyze_journal_entry(self, journal_entry: str) -> str:
        result = self.llama_llm.predict(
            PromptTemplate(LLAMA_JOURNAL_ANALYZE_TEMPLATE), journal_entry=journal_entry
        )

        return result


openai_client = OpenAIClient()


def get_openai_client() -> OpenAIClient:
    return openai_client
