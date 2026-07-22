from .base import DocumentationInput


class ArchitectureInput(DocumentationInput):
    """
    Architecture documentation input adapter.

    Converts architecture specifications into
    Markdown documentation.

    Future implementations may support:

    - System architecture documents
    - C4 models
    - ADRs (Architecture Decision Records)
    - Infrastructure diagrams
    - Design specifications

    The goal is to normalize architecture
    documentation into the same pipeline used
    by other documentation sources.
    """

    name = "Architecture Documentation"

    def __init__(self, path):
        self.path = path

    def generate_documentation(self) -> str:
        """
        Placeholder implementation.

        Future versions will parse structured
        architecture documents and generate
        documentation.
        """

        return f"""# Architecture Documentation

This is a placeholder implementation for the Architecture adapter.

Future versions will generate documentation from architecture specifications.

Source:

{self.path}
"""
