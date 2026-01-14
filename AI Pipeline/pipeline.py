import yaml
from pathlib import Path


def load_spec(path):
    """Load an OpenAPI spec from a YAML file."""
    with open(path, "r") as file:
        return yaml.safe_load(file)


def generate_docs(spec):
    """
    Generate basic Markdown documentation from an OpenAPI specification.
    """
    docs = []

    api_title = spec.get("info", {}).get("title", "API Documentation")
    docs.append(f"# {api_title}\n")

    paths = spec.get("paths", {})
    for endpoint, methods in paths.items():
        for method, details in methods.items():
            summary = details.get("summary", "No description provided.")
            docs.append(f"## {method.upper()} {endpoint}\n")
            docs.append(f"{summary}\n")

    return "\n".join(docs)


if __name__ == "__main__":
    spec_path = "API Specs/payments_api.yaml"
    output_dir = Path("Generated Docs")
    output_file = output_dir / "api.md"

    spec = load_spec(spec_path)
    docs = generate_docs(spec)

    output_dir.mkdir(exist_ok=True)

    with open(output_file, "w") as f:
        f.write(docs)

    print("Documentation generated successfully.")
