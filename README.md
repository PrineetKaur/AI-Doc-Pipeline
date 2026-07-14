# An End-to-End AI-assisted Pipeline for Documentation

This repository is a progressive, hands-on project focused on building **Efficient AI-Assisted Doc Pipelines**.

The goal is not to showcase a finished AI product, but to demonstrate **How AI Systems Should Evolve** _(starting from basic automation and gradually incorporating AI in a controlled, explainable way.)_

The project mirrors how real teams introduce AI into their documentation workflows: 

***Carefully, Incrementally***, but more importantly, governed with ***Human Oversight.**

![Preview of Developer Portal Demo](preview.png)

------------------------------------------------------------------------

## What this repository demonstrates

This project focuses on:

- Designing end-to-end documentation pipelines
- Working with structured technical inputs
- Generating consistent, repeatable documentation outputs
- Understanding WHERE AI adds value, and WHERE it should be governed
- Balancing developer experience (DX) with broader technical needs *(human and machine alike)*

APIs are used as the first example input, but the pipeline is intentionally designed to be extensible to other technical documentation domains, and consumable by both human readers and AI agents.

------------------------------------------------------------------------

## Project Layers
This project is organized around three architectural layers, each responsible for a different part of turning technical input into usable documentation.

### Layer 1 — Deterministic Generation
Reads structured technical input *(starting with OpenAPI/Swagger specs)* and produces a baseline Markdown document through fully deterministic, reproducible logic. No AI is involved. This layer is the source of truth throughout the project, and every other layer builds on top of it *(never replaces it)*.

### Layer 2 — AI-Assisted Enhancement
An optional editorial layer that improves the clarity, structure, and developer experience of Layer 1's output. It does not invent or modify technical facts, can be toggled on or off, and falls back safely to Layer 1's deterministic output if it fails. This is where the project's governance philosophy lives most visibly: AI augments, it doesn't replace.

### Layer 3 — Exposure & Agent Integration
Makes the pipeline callable by AI agents and external tools, via MCP, rather than only runnable as a local script. This layer depends on Layers 1 and 2 already being solid and governed; exposing an ungoverned pipeline to autonomous agents would defeat the purpose of everything built before it.

**To Note:** *Phase 2 uses a mock AI provider for local development and demonstration purposes. The mock provider simulates an AI-assisted documentation workflow without requiring an external LLM, API keys, or paid services. This allows anyone cloning the repository to understand and execute the complete documentation pipeline while keeping the project simple, reproducible, and cost-free. When using the project in a real-world scenario, the mock provider can be replaced by an external LLM (such as OpenAI or another compatible provider) through configuration, without changing the overall pipeline architecture.*

------------------------------------------------------------------------

## Repository structure

```
ai-doc-pipeline/
│
├── AI Pipeline Code/
│   ├── pipeline.py              # SOURCE: documentation pipeline logic
│   └── ai/
│       ├── __init__.py
│       ├── enhancer.py          # AI editor logic
│       ├── prompts.py           # Controlled AI instructions
│       └── mock_llm.py          # Local Mock AI (if you don't want to use an external LLM)
│
├── API Specs/                   # INPUT: structured technical specs
│   └── payments_api.yaml
│
├── Docs/
│   ├── final_architecture.md
│   └── pipeline_architecture_evolution.md
│
├── Generated Documentation/     # OUTPUT: generated documentation
│   ├── .gitkeep
│   └── api.md
│
├── MCP Server/                  # PLANNED (Phase 6): MCP tool exposure layer
│   ├── server.py
│   └── tools/
│       ├── parse_spec.py
│       ├── generate_baseline_doc.py
│       ├── enhance_with_ai.py
│       └── check_doc_drift.py
│
├── README.md                    
├── LICENSE
├── requirements.txt             # Minimal requirements for running the project
├── .env.example                 # Just an artifact for you to better understand "What environment variables does this project expect?"
```

Each folder has a clearly defined responsibility:
- **Source** – Documentation pipeline implementation
- **Input** – Structured technical specifications
- **Output** – Generated documentation
- **AI Layer** – Optional editorial enhancement

------------------------------------------------------------------------

## The Phased Roadmap

This repository is intentionally developed in **clear phases**, similar to a learning playground or to the evolution of internal tooling.

The phased progression below shows how each layer is built out over time. Phases 1 and 2 establish Layers 1 and 2; Phases 3–5 extend and strengthen them (new input types, audience awareness, governance); and Phase 6 builds Layer 3 on that foundation.


### Phase 1 — Deterministic pipeline 
- Structured input → Markdown output
- No AI
- Focus on correctness and reproducibility

### Phase 2 — AI-assisted API documentation 
- Improve clarity, structure, and examples using AI
- AI augments the pipeline, not replaces it
- Strong focus on developer experience (DX)

### Phase 3 — Multiple input types (current)
- Extend beyond APIs to:
  - SDKs / libraries
  - CLI tools
  - Configuration schemas
- Same pipeline, different parsers

### Phase 4 — Audience-aware documentation
- Generate documentation tailored for:
  - Developers
  - Product or platform users
  - Internal engineering teams

### Phase 5 — Documentation governance
- Style and terminology consistency
- Detection of ambiguity or drift
- Human-in-the-loop review patterns

### Phase 6 — Exposure & agent integration
- Expose core pipeline functions as MCP tools (`parse_spec`, `generate_baseline_doc`, `enhance_with_ai`)
- Add a `check_doc_drift` tool, building on the drift and ambiguity detection established in Phase 5
- Optionally, a lightweight Claude Skill that orchestrates these tools for common documentation tasks
- Makes the pipeline callable by AI agents and external MCP clients, not just runnable as a local script

Final Output: An end-to-end documentation pipeline with AI augmentation layer that is provider-agnostic. The pipeline can operate with a deterministic implementation, a local mock implementation for reproducible testing, or an external LLM provider without changing the surrounding system.

------------------------------------------------------------------------

## How to run the pipeline

From the repository root:

```bash
python3 "AI Pipeline Code/pipeline.py"
```

### Deterministic mode (default)

By default, the pipeline generates documentation using only the deterministic generation step.

No AI configuration is required.

### AI-assisted mode (optional)

To enable AI-assisted documentation enhancement:

```bash
export USE_AI=true
export OPENAI_API_KEY=your_api_key

python3 "AI Pipeline Code/pipeline.py"
```

After running:
- A Markdown file is generated inside `Generated Documentation/`
- The output can be reviewed, committed, and published (by you or AI, depending on whether you turn on AI)

To Note: 
- When AI is enabled, the deterministic documentation is generated first and then refined by the AI editor.
- If AI enhancement fails for any reason, the pipeline falls back gracefully to provide the deterministic output.

#### **Instructions for running the MCP server (Layer 3) will be added once Phase 6 is implemented.**
------------------------------------------------------------------------

## Why this project exists

This repository exists to explore:

- How technical documentation systems scale
- How AI fits into real documentation workflows
- How structure enables better automation
- How writers, DX engineers, and product teams collaborate through tooling

The emphasis is on **reasoning, structure, and evolution**, not just output.

------------------------------------------------------------------------

## About the approach

- Each phase builds on the previous one
- Complexity is introduced gradually
- Decisions are intentional and documented
- The project remains understandable at every stage

This mirrors how documentation platforms and internal tooling are built
in real organizations.

------------------------------------------------------------------------

## AI Pipeline Architecture

Rather than tightly coupling the pipeline to a single AI provider, the project separates documentation generation from AI enhancement.

The pipeline supports pluggable AI enhancement layers and intentionally treats AI as an **augmentation layer** *(not as a replacement for deterministic documentation generation).* 

The pipeline follows three core principles:

- **Deterministic first** — Structured technical specifications remain the authoritative source of documentation.
- **AI as an editor** — AI improves readability, structure, and developer experience without changing technical facts.
- **Graceful fallback** — If AI is unavailable, the deterministic documentation is still generated successfully.

This architecture demonstrates a practical approach to introducing AI into technical documentation workflows while maintaining transparency, reliability, and human oversight.

Also, a mock provider is included for local testing, while external LLM providers can be connected through configuration. The AI Interface doesn't know whether it is talking to *OpenAI, Claude, Gemini, Ollama, or a Mock AI*

Inspired by popular software engineering principles like: *abstraction, separation of concerns, avoiding vendor lock-in, safe experimentation, reproducibility*

------------------------------------------------------------------------

## Notes

All examples use simplified or fictional specifications to keep the project approachable and easy to evaluate. This repository demonstrates the architecture and reasoning behind AI-governed documentation pipelines. The same patterns that would apply to a production system are built here at a scale suited for learning, experimentation, and portfolio review.
