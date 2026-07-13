# Pipeline Architecture Evolution

> **Project:** AI-Doc-Pipeline\
> **Purpose:** Document the architectural evolution of the documentation
> pipeline throughout the project lifecycle.

------------------------------------------------------------------------

# Project Vision

The objective of AI-Doc-Pipeline is not to build a tool that simply
converts OpenAPI specifications into Markdown.

The goal is to demonstrate how a documentation platform can evolve from
a deterministic documentation generator into a modular, AI-augmented
documentation system capable of supporting multiple documentation
sources and multiple audiences while maintaining clear architectural
boundaries.

The project intentionally evolves in phases, with each phase introducing
a new architectural capability while preserving previous functionality.

------------------------------------------------------------------------

# Phase 1 --- Deterministic Documentation Generation

**Status:** ✅ Completed

## Problem

Technical documentation is frequently written manually, making it
difficult to keep documentation synchronized with API specifications.

## Solution

Generate documentation directly from an OpenAPI specification using a
deterministic parser.

## Architecture

``` text
          OpenAPI Specification
                   │
                   ▼
        Deterministic Generator
                   │
                   ▼
          Markdown Documentation
```

## Design Decisions

-   Deterministic generation ensures reproducible output.
-   Documentation is generated directly from the specification.
-   No external services are required.
-   The generated documentation becomes the single source of truth.

## Files Introduced

``` text
pipeline.py
payments_api.yaml
Generated Docs/api.md
```

## Key Takeaways

-   Deterministic systems are predictable and reproducible.
-   API specifications can serve as documentation sources.
-   Documentation generation should be automated whenever possible.

------------------------------------------------------------------------

# Phase 2 --- AI Augmentation Layer

**Status:** ✅ Completed

## Problem

Deterministic documentation is technically correct but often lacks
readability and editorial refinement.

## Solution

Introduce an optional AI enhancement layer after deterministic
generation while keeping deterministic output as the source of truth.

## Architecture

``` text
             OpenAPI Specification
                     │
                     ▼
      Deterministic Documentation Generator
                     │
                     ▼
              Markdown Draft
                     │
                     ▼
            AI Enhancement Layer
                     │
         ┌───────────┴───────────┐
         ▼                       ▼
  Mock AI Provider       OpenAI Provider
         │                       │
         └───────────┬───────────┘
                     ▼
          Enhanced Markdown Output
```

## Design Decisions

-   AI is optional.
-   Deterministic generation remains authoritative.
-   Provider abstraction avoids vendor lock-in.
-   Mock provider enables reproducible local development.
-   External providers can be connected through configuration.

## Files Introduced

``` text
ai/
    enhancer.py
    mock_llm.py
    prompts.py
```

## Key Takeaways

-   AI enhances deterministic systems instead of replacing them.
-   Provider abstraction enables flexibility.
-   Mock implementations simplify demonstrations.

------------------------------------------------------------------------

# Phase 3 --- Multi-Source Documentation Platform

**Status:** 🚧 In Progress

## Problem

A pipeline tightly coupled to OpenAPI cannot easily support additional
documentation sources.

## Solution

Introduce input adapters so every documentation source implements a
common interface while the pipeline remains unchanged.

## Current Architecture

``` text
               OpenAPI Specification
                       │
                       ▼
                OpenAPI Adapter
                       │
                       ▼
           Documentation Pipeline
                       │
                       ▼
            AI Enhancement Layer
                       │
             Generated Documentation
```

## Target Architecture

``` text
                Documentation Inputs
                        │
     ┌──────────┬──────────┬──────────┬──────────┬────────────┐
     ▼          ▼          ▼          ▼          ▼
 OpenAPI      SDK        CLI      Config   Architecture
     │          │          │          │          │
     └──────────┴──────────┴──────────┴──────────┘
                        │
                        ▼
             Documentation Pipeline
                        │
                        ▼
             AI Enhancement Layer
                        │
         ┌──────────────┴──────────────┐
         ▼                             ▼
    Mock Provider               OpenAI Provider
                        │
                        ▼
             Generated Documentation
```

## Design Decisions

-   Separate orchestration from parsing.
-   Introduce source-specific adapters.
-   Keep the pipeline source-agnostic.

## Files Introduced

Current:

``` text
inputs/
    openapi.py
```

Planned:

``` text
inputs/
    sdk.py
    cli.py
    config.py
    architecture.py
```

------------------------------------------------------------------------

# Phase 4 --- Audience-Aware Documentation

**Status:** 📋 Planned

## Architecture

``` text
          Documentation Pipeline
                   │
                   ▼
          Canonical Documentation
                   │
        ┌──────────┼──────────┐
        ▼          ▼          ▼
 Developer     Product     Support
 Documentation Documentation Documentation
```

------------------------------------------------------------------------

# Phase 5 --- Documentation Quality & Automation

**Status:** 📋 Planned

## Architecture

``` text
Documentation
       │
       ▼
Validation
       │
       ▼
Quality Metrics
       │
       ▼
CI/CD Pipeline
       │
       ▼
Published Documentation
```

------------------------------------------------------------------------

# Final Target Architecture

``` text
                        Documentation Sources
   ┌──────────┬──────────┬──────────┬──────────────┬──────────────┐
   ▼          ▼          ▼          ▼              ▼
 OpenAPI     SDK        CLI      Config      Architecture
   │          │          │          │              │
   └──────────┴──────────┴──────────┴──────────────┘
                         │
                         ▼
              Documentation Pipeline
                         │
         ┌───────────────┴───────────────┐
         ▼                               ▼
  Deterministic Generator         Validation Layer
         │                               │
         └───────────────┬───────────────┘
                         ▼
                  Markdown Draft
                         │
                         ▼
                 AI Enhancement Layer
         ┌───────────────┴────────────────┐
         ▼                                ▼
    Mock Provider                   OpenAI Provider
                         │
                         ▼
              Audience Generation
         ┌───────────────┼───────────────┐
         ▼               ▼               ▼
     Developers      Product Team    Support Team
                         │
                         ▼
               Final Documentation Set
```
