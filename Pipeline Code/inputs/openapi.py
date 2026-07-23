import yaml

from .base import DocumentationInput


class OpenAPIInput(DocumentationInput):
    """
    OpenAPI documentation input adapter.

    Converts an OpenAPI YAML specification
    into Markdown documentation.
    """

    name = "OpenAPI Specification"


    def __init__(self, path):
        self.path = path


    def load_spec(self):

        with open(self.path, "r") as file:
            return yaml.safe_load(file)


    def generate_documentation(self):

        spec = self.load_spec()

        docs = []

        info = spec.get("info", {})

        docs.append(
            f"# {info.get('title', 'API Documentation')}\n"
        )


        if info.get("version"):

            docs.append(
                f"**Version:** {info['version']}\n"
            )


        if info.get("description"):

            docs.append(
                f"{info['description']}\n"
            )


        servers = spec.get("servers", [])

        if servers:

            docs.append(
                "## Base URL\n"
            )

            docs.append(
                f"`{servers[0].get('url')}`\n"
            )


        docs.append("---\n")

        docs.append(
            "# Endpoints\n"
        )


        paths = spec.get("paths", {})


        for endpoint, methods in paths.items():

            for method, details in methods.items():

                docs.append(
                    f"## {method.upper()} {endpoint}\n"
                )


                docs.append(
                    f"**Summary:** {details.get('summary', 'No summary available.')}\n"
                )


                if details.get("description"):

                    docs.append(
                        f"**Description:** {details['description']}\n"
                    )


                parameters = details.get(
                    "parameters",
                    []
                )


                if parameters:

                    docs.append(
                        "### Parameters\n"
                    )


                    for parameter in parameters:

                        docs.append(
                            f"- **{parameter.get('name')}** ({parameter.get('in')})"
                        )


                    docs.append("\n")


                if "requestBody" in details:

                    docs.append(
                        "### Request Body\n"
                    )

                    docs.append(
                        "Request body required.\n"
                    )


                responses = details.get(
                    "responses",
                    {}
                )


                if responses:

                    docs.append(
                        "### Responses\n"
                    )


                    for code, response in responses.items():

                        docs.append(
                            f"- **{code}** — {response.get('description', '')}"
                        )


                    docs.append("\n")


                docs.append(
                    "---\n"
                )


        return "\n".join(docs)
