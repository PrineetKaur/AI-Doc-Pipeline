from .base import DocumentationInput


class CLIInput(DocumentationInput):
    """
    Command-Line Interface (CLI) documentation input adapter.

    Converts CLI command metadata into Markdown documentation.

    Future implementations may support:

    - Command definitions
    - Arguments
    - Flags
    - Subcommands
    - Usage examples

    The goal is to normalize CLI documentation
    into the same pipeline used by other
    documentation sources.
    """

    name = "CLI Documentation"

    def __init__(self, path):
        self.path = path

    def generate_documentation(self) -> str:
        """
        Placeholder implementation.

        Future versions will parse structured CLI
        specifications and generate documentation.
        """

        return f"""# CLI Documentation

This is a placeholder implementation for the CLI adapter.

Future versions will generate documentation from CLI specifications.

Source:

{self.path}
"""
