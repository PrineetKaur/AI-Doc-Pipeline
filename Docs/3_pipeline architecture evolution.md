
# Pipeline Architecture Evolution

> **Purpose:** Document the architectural evolution of the documentation pipeline throughout the project lifecycle.

------------------------------------------------------------------------

## Project Vision

The objective of AI-Doc-Pipeline is not to build a tool that simply converts OpenAPI specifications into Markdown.

The goal is to demonstrate how a documentation platform can evolve from a deterministic documentation generator into a modular, AI-augmented documentation system capable of supporting multiple documentation sources and multiple audiences while maintaining clear architectural boundaries.

The project intentionally evolves in phases, with each phase introducing a new architectural capability while preserving previous functionality.

------------------------------------------------------------------------

## Phase 1 - Deterministic Documentation Generation

**Status:** ✅ Completed

### Problem

Technical documentation is frequently written manually, making it difficult to keep documentation synchronized with API specifications.

### Solution

Generate documentation directly from an OpenAPI specification using a deterministic parser.

### Architecture

``` text
          OpenAPI Specification
                    │
                    ▼
         Deterministic Generator
                    │
                    ▼
          Markdown Documentation
```

### Design Decisions

-   Deterministic generation ensures reproducible output.
-   Documentation is generated directly from the specification.
-   No external services are required.
-   The generated documentation becomes the single source of truth.

### Files Introduced

``` text
pipeline.py
payments_api.yaml
Generated Documentation/api.md
```

### Key Takeaways

-   Deterministic systems are predictable and reproducible.
-   API specifications can serve as documentation sources.
-   Documentation generation should be automated whenever possible.

------------------------------------------------------------------------

## Phase 2 - AI Augmentation Layer

**Status:** ✅ Completed

### Problem

Deterministic documentation is technically correct but often lacks readability and editorial refinement.

### Solution

Introduce an optional AI enhancement layer after deterministic generation while keeping deterministic output as the source of truth.

### Architecture

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
    Mock AI Provider        OpenAI Provider
           │                       │
           └───────────┬───────────┘
                       ▼
           Enhanced Markdown Output
```

### Design Decisions

-   AI is optional.
-   Deterministic generation remains authoritative.
-   Provider abstraction avoids vendor lock-in.
-   Mock provider enables reproducible local development.
-   External providers can be connected through configuration.

### Files Introduced

``` text
ai/
    enhancer.py
    mock_llm.py
    prompts.py
```

### Key Takeaways

-   AI enhances deterministic systems instead of replacing them.
-   Provider abstraction enables flexibility.
-   Mock implementations simplify demonstrations.

------------------------------------------------------------------------

## Phase 3 - Decoupling the Pipeline from Documentation Sources

**Status:** 🚧 In Progress

### Problem

The documentation pipeline was tightly coupled to a single documentation source.

Although the system successfully generated documentation from OpenAPI specifications, the orchestration layer had direct knowledge of the input format. Supporting additional documentation sources would require modifying the pipeline itself, making the architecture increasingly difficult to extend and maintain.

### Solution

Introduce an adapter-based architecture that separates documentation parsing from pipeline orchestration.

Rather than depending on a specific documentation source, the pipeline depends on a common input abstraction. Each documentation source becomes responsible for translating its own structure into a unified format understood by the pipeline.

This transforms the pipeline from a source-specific implementation into a source-agnostic platform.

### Current Architecture

```text
          OpenAPI Specification
                    │
                    ▼
          Documentation Pipeline
                    │
                    ▼
          Deterministic Generator
                    │
                    ▼
           AI Enhancement Layer
                    │
                    ▼
         Generated Documentation
```

### Architectural Refactor

```text
           Documentation Source
                    │
                    ▼
              Input Adapter
                    │
                    ▼
          Documentation Pipeline
                    │
                    ▼
         Deterministic Generator
                    │
                    ▼
          AI Enhancement Layer
                    │
                    ▼
         Generated Documentation
```

### Target Architecture

```text
                 Documentation Sources

              OpenAPI    SDK      CLI
                 │        │        │
                 ▼        ▼        ▼
              OpenAPI    SDK      CLI
              Adapter  Adapter   Adapter
                 │        │        │
                 └────────┴────────┘
                          │
                          ▼
                Documentation Pipeline
                          │
                          ▼
               Deterministic Generator
                          │
                          ▼
                AI Enhancement Layer
               ┌──────────┴──────────┐
               ▼                     ▼
         Mock Provider        OpenAI Provider
                          │
                          ▼
               Generated Documentation
```

### Design Decisions

- Decouple pipeline orchestration from documentation parsing.
- Introduce source-specific adapters behind a common interface.
- Keep the pipeline independent of documentation source formats.
- Enable new documentation sources without modifying the pipeline.
- Apply the Open/Closed Principle by extending the system through adapters rather than changing the orchestration layer.

### Files Introduced

Current

```text
inputs/
    base.py
    openapi.py
```

Planned

```text
inputs/
    sdk.py
    cli.py
    config.py
    architecture.py
```

### Key Takeaways

- The pipeline becomes source-agnostic.
- New documentation sources are introduced through adapters.
- The orchestration layer remains stable as the platform evolves.
- Architectural extensibility is achieved through abstraction rather than modification.

------------------------------------------------------------------------

## Phase 4 - Audience-Aware Documentation

**Status:** 📋 Planned

### Architecture

``` text
          Documentation Pipeline
                    │
                    ▼
         Canonical Documentation
                    │
         ┌──────────┼──────────┐
         ▼          ▼          ▼
    Developer    Product    Support
Documentation Documentation Documentation
```

------------------------------------------------------------------------

## Phase 5 - Documentation Quality & Automation

**Status:** 📋 Planned

### Architecture

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

## Long-Term Platform Architecture

``` text
                        Documentation Sources
          ┌──────────┬──────────┬───────────┬────────────┐
          ▼          ▼          ▼           ▼            ▼
       OpenAPI      SDK        CLI        Config    Architecture
          │          │          │           │            │
          └──────────┴──────────┴───────────┴────────────┘
                                │
                                ▼
                      Documentation Pipeline
                                │
                ┌───────────────┴───────────────┐
                ▼                               ▼
      Deterministic Generator             Validation Layer
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
