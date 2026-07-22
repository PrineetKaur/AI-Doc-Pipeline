from .base import DocumentationInput


class SDKInput(DocumentationInput):
    """
    SDK documentation input adapter.

    Converts SDK metadata into Markdown documentation.

    Future implementations may support:

    - Python packages
    - Java SDKs
    - Node.js libraries
    - .NET SDKs

    The goal is to normalize SDK documentation
    into the same pipeline used by other
    documentation sources.
    """

    name = "SDK Documentation"

    def __init__(self, path):
        self.path = path

    def generate_documentation(self) -> str:
        """
        Placeholder implementation.

        Future versions will parse structured SDK
        metadata and generate documentation.
        """

        return f"""# SDK Documentation

This is a placeholder implementation for the SDK adapter.

Future versions will generate documentation from SDK metadata.

Source:

{self.path}
"""
