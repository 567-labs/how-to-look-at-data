# How to Look at Data: A Complete Guide to RAG System Analysis and Improvement

> **A three-part series on systematically analyzing and improving RAG systems through topic modeling, custom summarization, and production classifiers from [improvingrag.com](https://improvingrag.com) and [ChromaDB](https://chromadb.com).**

> Prerequisites: Make sure that you've downloaded and saved the 560 conversations to a file at the path `./data/conversations.json`

## Overview

This repository demonstrates a complete methodology for transforming raw user queries into actionable RAG system improvements. Using 560 real user queries from Weights & Biases documentation, you'll learn to move from reactive to proactive RAG optimization through systematic analysis.

**The Journey**: Discover patterns → Validate with better summaries → Monitor continuously through classification → Prioritize improvements based on real usage data.

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/567-labs/how-to-look-at-data.git
   cd how-to-look-at-data
   ```

2. Install dependencies (using uv):

   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   uv sync
   ```

3. Set up your environment variables:
   - You will need a `GOOGLE_API_KEY` or an `OPENAI_API_KEY` for running this topic modelling process. We're using the OpenAI Text-Embedding-3-Small embeddings for clustering and the Gemini-2.0-flash models for summarisation (used by `kura`).

## Tools

### Notebook Watcher

This repository includes a file watcher that automatically converts Jupyter notebooks to Markdown format whenever they're saved. This is useful for version control and documentation.

**Usage:**

```bash
# Watch current directory and save to ./md/
./watch_notebooks.py

# Watch specific directory
./watch_notebooks.py /path/to/notebooks

# Custom output directory
./watch_notebooks.py -o /custom/output
```

The watcher will:
- Convert all existing notebooks on startup
- Monitor for changes and auto-convert on save
- Display colorful progress with Rich console output
- Save all markdown files to the `md/` directory by default

## Notebooks

### 1. Cluster Conversations: Discovering User Query Patterns

**What You'll Learn:**
- How to prepare query data for effective topic modeling using Kura conversation objects
- Running hierarchical topic clustering with LLM-enhanced summarization
- Analyzing cluster themes and distribution patterns to identify high-impact improvement areas

**What You'll Discover:**
Just three major topics account for over two-thirds of all user queries, with artifact management appearing as a dominant theme across 61% of conversations. However, you'll also discover that default summaries are too generic, missing crucial details about specific W&B features—setting up the need for custom summarization.

**Key Methodology:**
- Uses Kura's LLM-enhanced clustering approach that generates meaningful summaries rather than just numeric vectors
- Transforms raw JSON query-document pairs into structured conversation objects
- Creates topic hierarchies showing relationships between user query themes

### 2. Better Summaries: Building Domain-Specific Clustering

**What You'll Learn:**
- Building custom summary models with specialized prompts for domain-specific information extraction
- Comparing generic vs. domain-specific summarization approaches and their impact on clustering
- Implementing length constraints and consistent formatting for focused, actionable summaries

**What You'll Discover:**
Transform nine generic clusters into three highly actionable categories: Access Controls (data export/security), Deployment (service integration/auth), and Experiment Management (artifacts/visualization/multi-GPU). This dramatic improvement in cluster quality provides the foundation for building production classifiers.

**Key Innovation:**
The `WnBSummaryModel` class extends Kura's base summarization with W&B-specific prompts that:
- Identify specific W&B features (Artifacts, Configs, Reports)
- Clearly state user problems and goals
- Generate concise, consistent 25-word summaries

### 3. Classifiers: Building Production Query Classifiers for RAG Systems

**What You'll Learn:**
- Creating production-ready classifiers using the `instructor-classify` framework
- Generating weak labels automatically and designing systematic workflows for human verification
- Achieving high classification accuracy through systematic prompt engineering and few-shot examples

**What You'll Achieve:**
Build a classifier that achieves 90.9% accuracy (improving from a 72.7% baseline) and discover that just three categories (artifacts, integrations, visualizations) account for 50% of all user conversations, giving you clear targets for maximum impact improvements.

**Production Impact:**
- **Detect Production Drift**: Identify when certain query types suddenly increase, signaling emerging issues
- **Route Queries Intelligently**: Direct questions to specialized retrieval pipelines based on category
- **Prioritize Improvements**: Focus engineering resources on high-volume, low-satisfaction query types
- **Measure Impact**: Track how changes affect different user segments over time

## Key Technologies

- **Kura**: LLM-enhanced topic modeling and clustering
- **instructor-classify**: Production-ready classification framework
- **OpenAI Embeddings**: Text-Embedding-3-Small for semantic similarity
- **Gemini 2.0 Flash**: Advanced summarization and classification

## Dataset

Working with 560 real user queries from Weights & Biases documentation, each manually labeled with relevant retrieved documents. This dataset provides direct insight into how users interact with ML experiment tracking documentation and serves as a gold standard for understanding user intent patterns.

## About

This repository was created for the **AI Engineering Summit**. It demonstrates practical techniques for analyzing and improving Retrieval-Augmented Generation (RAG) systems using real-world data and modern topic modeling tools.

The methodology shown here transforms RAG systems from reactive (waiting for user complaints) to proactive (identifying problems before users complain and prioritizing fixes based on systematic analysis rather than the loudest feedback).
