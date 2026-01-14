# AI Pipeline for Technical Documentation

An end-to-end automated workflow that transforms an OpenAPI specification into clean, structured
API documentation using AI, with an optional human review step and
static site generation.

![Preview of Developer Portal Demo](preview.png)

------------------------------------------------------------------------

## Project Overview

This project demonstrates how AI can be integrated into the technical
documentation lifecycle. The pipeline automatically:

-   Reads an OpenAPI/Swagger YAML specification\
-   Extracts API endpoints\
-   Generates high‑quality Markdown documentation using a large language
    model\
-   Outputs AI drafts into `generated-docs/`\
-   Allows editors to refine content in `reviewed-docs/`\
-   Publishes a documentation site using MkDocs\
-   Optionally deploys via GitHub Actions → GitHub Pages

It's designed as a portfolio project for **Technical Writers, Developer
Experience (DX) Engineers, and Product Documentation Specialists**.

------------------------------------------------------------------------
## Technologies Used

-   **Python**
-   **OpenAI GPT models**
-   **MkDocs**
-   **PyYAML**
-   **GitHub Actions**
-   **Markdown Automation**
-   **AI-driven Content Generation**

------------------------------------------------------------------------
## Why This Project?

This pipeline showcases your ability to:

-   Design end‑to‑end developer documentation workflows\
-   Integrate AI into production processes\
-   Work with API specs\
-   Build automated tooling\
-   Structure scalable documentation systems

**This is an excellent addition to any portfolio in:**

-   Technical Writing\
-   Developer Experience (DX)\
-   API Documentation\
-   AI + Documentation Systems\
-   Product Knowledge Engineering

------------------------------------------------------------------------


## Repository Structure

    ai-doc-pipeline/
    │
    ├── api-specs/                # Input OpenAPI specifications
    │   └── payments_api.yaml
    │
    ├── generated-docs/           # AI‑generated drafts
    │   └── post_v1_payments.md
    │
    ├── reviewed-docs/            # Manually edited final docs
    │   └── placeholder.md
    │
    ├── site/                     # MkDocs static site
    │   ├── mkdocs.yml
    │   └── docs/
    │       └── index.md
    │
    ├── AI Pipeline/                     
    │   └── pipeline.py           # Main automation script        
    ├── requirements.txt
    │
    └── .github/
        └── workflows/
            └── ci.yml            # Optional GitHub Actions deployment

------------------------------------------------------------------------

## How It Works

### **1️⃣ Input: API Specification**

Place any OpenAPI file inside:

    api-specs/

Example included: - `payments_api.yaml`

------------------------------------------------------------------------

### **2️⃣ AI Generation**

Run:

    python pipeline.py

The script:

-   Loads the OpenAPI spec\
-   Iterates through paths and methods\
-   Sends structured prompts to the AI model\
-   Creates Markdown documentation files

Output appears in:

    generated-docs/

------------------------------------------------------------------------

### **3️⃣ Human Review (Optional but Recommended)**

Move or copy files to:

    reviewed-docs/

Here you can refine:

-   Wording\
-   Formatting\
-   Clarify ambiguous API behavior\
-   Add advanced examples or context

------------------------------------------------------------------------

### **4️⃣ Documentation Site**

Inside the `site/` folder:

    cd site
    mkdocs serve

Then open:

    http://127.0.0.1:8000

The MkDocs config pulls in:

-   Generated docs\
-   Reviewed docs\
-   Homepage files

------------------------------------------------------------------------

### **5️⃣ Optional: Deploy Automatically**

The included GitHub Actions workflow:

    .github/workflows/ci.yml

Allows:

-   Auto-regeneration of docs\
-   Auto-build of MkDocs site\
-   Auto-deploy to GitHub Pages

Just add:

    OPENAI_API_KEY

to your repository secrets.

------------------------------------------------------------------------

## Requirements

Install dependencies:

    pip install -r requirements.txt

Set your OpenAI key:

    export OPENAI_API_KEY="sk-xxxx"

------------------------------------------------------------------------


## Contact

Feel free to connect or reach out for collaborations, feedback, or
enhancements.

------------------------------------------------------------------------

## If You Like This Project...

Don't forget to give this repo a **star** ⭐ on GitHub!
