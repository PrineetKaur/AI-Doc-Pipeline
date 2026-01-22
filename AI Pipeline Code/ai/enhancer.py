import os
from openai import OpenAI
from .prompts import SYSTEM_PROMPT


def enhance_markdown(markdown_text: str) -> str:
    """
    Uses an LLM as an editorial step to improve clarity and DX.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": markdown_text}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content
