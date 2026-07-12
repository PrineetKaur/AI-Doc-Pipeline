print("Pipeline started")

import os
import yaml
from pathlib import Path

# Optional AI enhancer
USE_AI = os.getenv("USE_AI", "false").lower() == "true"

if USE_AI:
    try:
        from ai.enhancer import enhance_markdown
    except ImportError:
        USE_AI = False


def load_spec(path):
    """Load an OpenAPI spec from a YAML file."""
    with open(path, "r") as file:
        return yaml.safe_load(file)


def generate_docs(spec):
    """
    Generate Markdown documentation from an OpenAPI specification.
    """

    docs = []

    info = spec.get("info", {})

    docs.append(f"# {info.get('title', 'API Documentation')}\n")

    docs.append(f"**Version:** {info.get('version', 'N/A')}\n")

    if info.get("description"):
        docs.append(f"{info['description']}\n")

    servers = spec.get("servers", [])
    if servers:
        docs.append("## Base URL\n")
        docs.append(f"`{servers[0]['url']}`\n")

    docs.append("---\n")

    docs.append("# Endpoints\n")

    paths = spec.get("paths", {})

    for endpoint, methods in paths.items():

        for method, details in methods.items():

            docs.append(f"## {method.upper()} {endpoint}\n")

            docs.append(
                f"**Summary:** {details.get('summary','No summary available.')}\n"
            )

            if details.get("description"):
                docs.append(
                    f"**Description:** {details['description']}\n"
                )

            parameters = details.get("parameters", [])

            if parameters:

                docs.append("### Parameters\n")

                for parameter in parameters:

                    docs.append(
                        f"- **{parameter['name']}** ({parameter['in']})"
                    )

            if "requestBody" in details:
                docs.append("\n### Request Body\n")
                docs.append("Request body required.\n")

            responses = details.get("responses", {})

            if responses:

                docs.append("\n### Responses\n")

                for code, response in responses.items():

                    docs.append(
                        f"- **{code}** — {response.get('description','')}"
                    )

            docs.append("\n---\n")

    return "\n".join(docs)
