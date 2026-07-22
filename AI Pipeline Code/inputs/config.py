from .base import DocumentationInput


class ConfigurationInput(DocumentationInput):
    """
    Configuration documentation input adapter.

    Converts structured configuration metadata
    into Markdown documentation.

    Future implementations may support:

    - YAML configuration
    - JSON configuration
    - TOML configuration
    - Environment variables
    - Infrastructure configuration

    The goal is to normalize configuration
    documentation into the same pipeline used
    by other documentation sources.
    """

    name = "Configuration Documentation"

    def __init__(self, path):
        self.path = path

    def generate_documentation(self) -> str:
        """
        Placeholder implementation.

        Future versions will parse structured
        configuration files and generate
        documentation.
        """

        return f"""# Configuration Documentation

This is a placeholder implementation for the Configuration adapter.

Future versions will generate documentation from configuration files.

Source:

{self.path}
"""
