def enhance_with_mock(markdown_text: str) -> str:
    """
    Simulates an AI enhancement step without calling an external LLM.
    """

    banner = (
        "> **Mock AI Enhancement**\n"
        "> This documentation has been processed using the built-in mock AI provider.\n"
        "> The content demonstrates the AI enhancement stage without requiring an external API.\n\n"
    )

    enhanced = markdown_text.replace(
        "# Endpoints",
        "# Endpoints\n\n"
        "The following endpoints are available in this API."
    )

    return banner + enhanced
