import os

from .prompts import SYSTEM_PROMPT
from .mock_llm import enhance_with_mock


def enhance_markdown(markdown_text: str, provider: str = "mock") -> str:
    """
    Routes documentation enhancement to the selected AI provider.

    Supported providers:
    - mock
    - openai
    """

    provider = provider.lower()

    if provider == "mock":
        return enhance_with_mock(markdown_text)

    elif provider == "openai":

        from openai import OpenAI

        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": markdown_text
                }
            ],
            temperature=0.2
        )

        return response.choices[0].message.content

    else:

        raise ValueError(
            f"Unsupported AI provider: {provider}"
        )
