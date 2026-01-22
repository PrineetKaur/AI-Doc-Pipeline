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
    Generate deterministic Markdown documentation from an OpenAPI specification.
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

    # Phase 2: Optional AI enhancement
    if USE_AI:
        try:
            docs = enhance_markdown(docs)
            print("AI enhancement applied.")
        except Exception as e:
            print(f"AI enhancement failed, using deterministic output: {e}")

    output_dir.mkdir(exist_ok=True)

    with open(output_file, "w") as f:
        f.write(docs)

    print("Documentation generated successfully.")
