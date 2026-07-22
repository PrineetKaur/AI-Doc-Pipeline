from .openapi import OpenAPIInput
from .sdk import SDKInput
from .cli import CLIInput
from .config import ConfigurationInput
from .architecture import ArchitectureInput


class InputFactory:
    """
    Creates the appropriate documentation input adapter.

    The pipeline delegates adapter selection to this
    factory instead of depending on concrete input
    implementations directly.
    """

    _INPUT_TYPES = {
        "openapi": OpenAPIInput,
        "sdk": SDKInput,
        "cli": CLIInput,
        "config": ConfigurationInput,
        "architecture": ArchitectureInput,
    }

    @classmethod
    def create(cls, input_type: str, path: str):
        """
        Create a documentation input adapter.

        Parameters
        ----------
        input_type
            Type of documentation source.

        path
            Location of the source document.
        """

        adapter = cls._INPUT_TYPES.get(input_type.lower())

        if adapter is None:
            raise ValueError(
                f"Unsupported documentation input: {input_type}"
            )

        return adapter(path)
