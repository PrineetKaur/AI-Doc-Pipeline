import yaml
from pathlib import Path

def load_spec(path):
    with open(path) as f:
        return yaml.safe_load(f)

def generate_docs(spec):
    docs = []
    for path, methods in spec["paths"].items():
        for method, details in methods.items():
            docs.append(f"# {method.upper()} {path}\n\n{details.get('summary')}")
    return "\n\n".join(docs)

if _name_ == "_main_":
    spec = load_spec("api-specs/payments_api.yaml")
    output = generate_docs(spec)

    Path("generated-docs").mkdir(exist_ok=True)
    with open("generated-docs/api.md", "w") as f:
        f.write(output)

    print("Docs generated!")
