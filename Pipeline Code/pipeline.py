import os

from pathlib import Path

from inputs.factory import InputFactory


USE_AI = os.getenv("USE_AI", "false").lower() == "true"

if USE_AI:

    try:

        from ai.enhancer import enhance_markdown

    except ImportError:

        USE_AI = False


def main():

    # ------------------------------------------------------------------
    # Documentation source configuration
    # ------------------------------------------------------------------

    INPUT_TYPE = "openapi"

    INPUT_PATH = "API Specs/payments_api.yaml"

    # ------------------------------------------------------------------

    output_dir = Path("Generated Documentation")

    output_file = output_dir / "api.md"

    print("Loading documentation input...")

    documentation_input = InputFactory.create(
        input_type=INPUT_TYPE,
        path=INPUT_PATH,
    )

    print(
        f"Processing input type: {documentation_input.name}"
    )

    print("Generating documentation draft...")

    docs = documentation_input.generate_documentation()

    if USE_AI:

        provider = os.getenv(
            "AI_PROVIDER",
            "mock",
        )

        print(
            f"AI provider selected: {provider}"
        )

        try:

            docs = enhance_markdown(
                markdown_text=docs,
                provider=provider,
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
