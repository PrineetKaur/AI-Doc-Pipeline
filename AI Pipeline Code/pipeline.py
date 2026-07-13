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
    """
    Load an OpenAPI specification from a YAML file.
    """
    with open(path, "r") as file:
        return yaml.safe_load(file)


def generate_docs(spec):
    """
    Generate Markdown documentation from an OpenAPI specification.
    """

    docs = []

    info = spec.get("info", {})

    docs.append(f"# {info.get('title', 'API Documentation')}\n")

    if info.get("version"):
        docs.append(f"**Version:** {info['version']}\n")

    if info.get("description"):
        docs.append(f"{info['description']}\n")

    servers = spec.get("servers", [])

    if servers:
        docs.append("## Base URL\n")
        docs.append(f"`{servers[0].get('url')}`\n")

    docs.append("---\n")

    docs.append("# Endpoints\n")

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

            parameters = details.get("parameters", [])

            if parameters:
                docs.append("### Parameters\n")

                for parameter in parameters:
                    docs.append(
                        f"- **{parameter.get('name')}** ({parameter.get('in')})"
                    )

                docs.append("\n")

            if "requestBody" in details:
                docs.append("### Request Body\n")
                docs.append(
                    "Request body required.\n"
                )

            responses = details.get("responses", {})

            if responses:
                docs.append("### Responses\n")

                for code, response in responses.items():

                    docs.append(
                        f"- **{code}** — {response.get('description', '')}"
                    )

                docs.append("\n")

            docs.append("---\n")

    return "\n".join(docs)


if __name__ == "__main__":

    spec_path = "API Specs/payments_api.yaml"

    output_dir = Path("Generated Docs")
    output_file = output_dir / "api.md"

    print("Loading API specification...")

    spec = load_spec(spec_path)

    print("Generating documentation draft...")

    docs = generate_docs(spec)

    # Optional AI enhancement
    if USE_AI:

        provider = os.getenv("AI_PROVIDER", "mock")

        try:
            print(f"Running AI enhancement ({provider})...")

            docs = enhance_markdown(
                docs,
                provider=provider
            )

            print("AI enhancement applied.")

        except Exception as e:

            print(
                f"AI enhancement failed, using deterministic output: {e}"
            )

    output_dir.mkdir(exist_ok=True)

    with open(output_file, "w") as file:
        file.write(docs)

    print("Documentation generated successfully.")
    print(f"Output: {output_file}")
