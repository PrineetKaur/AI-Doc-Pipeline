import os
from pathlib import Path

from inputs.openapi import OpenAPIInput


USE_AI = os.getenv("USE_AI", "false").lower() == "true"


if USE_AI:
    try:
        from ai.enhancer import enhance_markdown
    except ImportError:
        USE_AI = False


def main():

    spec_path = "API Specs/payments_api.yaml"

    output_dir = Path("Generated Docs")
    output_file = output_dir / "api.md"


    print("Loading documentation input...")


    # Phase 3:
    # Input type is now abstracted.
    # Today: OpenAPI
    # Future: SDK, CLI, Config, Architecture docs

    documentation_input = OpenAPIInput(spec_path)


    print(
        f"Processing input type: {documentation_input.name}"
    )


    print("Generating documentation draft...")


    docs = documentation_input.generate_documentation()


    if USE_AI:

        provider = os.getenv(
            "AI_PROVIDER",
            "mock"
        )

        print(
            f"AI provider selected: {provider}"
        )

        try:

            docs = enhance_markdown(
                markdown_text=docs,
                provider=provider
            )

            print(
                "AI enhancement applied successfully."
            )

        except Exception as error:

            print(
                f"AI enhancement failed: {error}"
            )

            print(
                "Using deterministic documentation."
            )


    output_dir.mkdir(
        exist_ok=True
    )


    with open(output_file, "w") as file:
        file.write(docs)


    print(
        "Documentation generated successfully."
    )

    print(
        f"Output: {output_file}"
    )



if __name__ == "__main__":
    main()
