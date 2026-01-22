# AI Pipeline for Technical Documentation

This repository is a progressive, hands-on project focused on building **Efficient AI-Assisted Doc Pipelines** for Technical Products.

The goal is not to showcase a finished AI product, but to demonstrate **How AI Systems Should Evolve** _(starting from basic automation and gradually incorporating AI in a controlled, explainable way.)_

The project mirrors how real teams introduce AI into their documentation workflows: 

***Carefully, Incrementally***, but more importantly, governed with ***Human Oversight.***

![Preview of Developer Portal Demo](preview.png)

------------------------------------------------------------------------

## What this repository demonstrates

This project focuses on:

- Designing **end-to-end documentation pipelines**
- Working with **structured technical inputs**
- Generating **consistent, repeatable documentation outputs**
- Understanding WHERE ***AI adds value***, and WHERE it should be **Governed**
- Balancing **developer experience (DX)** with broader technical user needs

APIs are used as the first example input, but the pipeline is intentionally designed to be extensible to other technical documentation domains.

------------------------------------------------------------------------

## Previous project state (Phase 1)

At its current stage, this repository contains a **fully working,
non-AI documentation pipeline**.

The pipeline:

- Reads a structured OpenAPI (Swagger) YAML file
- Extracts relevant technical information
- Generates Markdown documentation
- Writes the output to a version-controlled folder
- Produces deterministic, reproducible results

This phase establishes a strong foundation before introducing AI.

## Current project state (Phase 2)

At this stage, the repository contains a **working AI-assisted documentation pipeline** that builds directly on the deterministic foundation established in Phase 1.

The pipeline now operates in two distinct steps:

1. **Deterministic generation**
   - Reads a structured OpenAPI (Swagger) YAML file
   - Extracts endpoints and summaries
   - Produces a baseline Markdown document

2. **Optional AI-assisted enhancement**
   - Uses an LLM as an editorial layer
   - Improves clarity, structure, and developer experience
   - Does not invent or modify technical facts
   - Can be enabled or disabled via configuration

Key characteristics of Phase 2:

- The deterministic pipeline remains the source of truth
- AI is used only to improve readability and usability
- Output remains reproducible when AI is disabled
- The same command and output file are preserved
- Failures in the AI layer fall back safely to deterministic output

This phase demonstrates how AI can be introduced into documentation systems
**incrementally, transparently, and with strong governance**.

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
│       └── prompts.py           # Controlled AI instructions
│
├── API Specs/                   # INPUT: structured technical specs
│   └── payments_api.yaml
│
├── Generated Docs/              # OUTPUT: generated documentation
│   ├── .gitkeep
│   └── api.md
│
├── README.md                    
├── LICENSE
├── requirements.txt             # Minimal requirements for running the project
├── .env.example                 # Just an artifact for you to better understand “What environment variables does this project expect?”
```


Each folder has a clear responsibility:
- **Source**: how documentation is generated
- **Input**: what is being documented
- **Output**: what users ultimately read

------------------------------------------------------------------------

## How to run the pipeline (current version)

From the repository root, run the following:

If you want Deterministic Output only ⤵️

```bash                          
python3 "AI Pipeline Code/pipeline.py"        
```

#If you want AI-reviewed for better structure, clarity, and improved DevEx ⤵️

```bash
export USE_AI=true                                    
export OPENAI_API_KEY=your_key
python3 "AI Pipeline Code/pipeline.py"
```

After running:
- A Markdown file is generated inside `Generated Docs/`
- The output can be reviewed, committed, and published if you ran without AI, or else the output would be after AI-assisted enhancements


------------------------------------------------------------------------

## Planned project progression

This repository is intentionally developed in **clear phases**, similar to
a learning playground or internal tooling evolution.

### Phase 1 — Deterministic pipeline (current)
- Structured input → Markdown output
- No AI
- Focus on correctness and reproducibility

### Phase 2 — AI-assisted API documentation
- Improve clarity, structure, and examples using AI
- AI augments the pipeline, not replaces it
- Strong focus on developer experience (DX)

### Phase 3 — Multiple input types
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

## Notes

All examples use simplified or fictional specifications.
This repository is intended for learning, experimentation, and portfolio
demonstration — not as a production-ready documentation system.
