from abc import ABC, abstractmethod


class DocumentationInput(ABC):
    """
    Base interface for all documentation input sources.

    Future input types should implement this interface:

    - OpenAPI specifications
    - SDK documentation
    - CLI documentation
    - Configuration schemas
    - Architecture documents
    """

    name = "Unknown Input"

    @abstractmethod
    def generate_documentation(self) -> str:
        """
        Convert the input source into documentation markdown.
        """

        pass
