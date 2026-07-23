import os

from .prompts import SYSTEM_PROMPT
from .mock_llm import enhance_with_mock


def enhance_markdown(markdown_text: str, provider: str = "mock") -> str:
    """
    Enhance generated Markdown using the selected AI provider.

    Supported providers:
    - mock (default)
    - openai
    """

    provider = provider.lower().strip()

    # -----------------------------
    # Mock provider
    # -----------------------------
    if provider == "mock":

        print("Using mock AI provider.")

        return enhance_with_mock(markdown_text)

    # -----------------------------
    # OpenAI provider
    # -----------------------------
    if provider == "openai":

        print("Using OpenAI provider.")

        api_key = os.getenv("OPENAI_API_KEY")

        if not api_key:
            raise ValueError(
                "OPENAI_API_KEY environment variable is not set."
            )

        from openai import OpenAI

        client = OpenAI(api_key=api_key)

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

    # -----------------------------
    # Unknown provider
    # -----------------------------
    raise ValueError(
        f"Unsupported AI provider: '{provider}'"
    )
