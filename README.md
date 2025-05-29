# Chroma Workshop: Topic Modeling for RAG Systems

> Prerequisites: Make sure that you've downloaded and saved the 560 conversations to a file at the path `./data/conversations.json`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/567-labs/how-to-look-at-data.git
   cd how-to-look-at-data
   ```

2. Install dependencies (using uv):

   ```bash
   uv pip install -r pyproject.toml
   ```

3. Set up your environment variables:
   - You will need an `OPENAI_API_KEY` for running this topic modelling proccess. We're using the OpenAI Text-Embedding-3-Small embeddings for clustering and OpenAI models for summarisation (used by `kura`).

## Notebooks

### 1. [Cluster Conversations](./1.%20Cluster%20Conversations.ipynb)

Discover patterns in 560 real user queries from Weights & Biases documentation using Kura's LLM-enhanced topic modeling.

**You'll learn:**

- How topic modeling reveals query patterns invisible to keyword analysis
- Converting raw queries into clustered insights using embeddings
- Why default summaries miss critical domain-specific details

### 2. [Better Summaries](./2.%20Better%20Summaries.ipynb)

Transform generic clustering results into precise, actionable insights with custom summarization models.

**You'll learn:**

- Building domain-specific summary models for your use case
- How better summaries dramatically improve clustering quality
- Reducing noise to focus on what matters for your users

### 3. [Classifiers](./3.%20Classifiers.ipynb)

Build production-ready classifiers that achieve 90%+ accuracy through systematic prompt engineering.

**You'll learn:**

- Creating weak labels for rapid dataset creation
- Iterative prompt improvement techniques
- Deploying classifiers to monitor query patterns in real-time

## About

This repository was created for the **AI Engineering Summit**. It demonstrates practical techniques for analyzing and improving Retrieval-Augmented Generation (RAG) systems using real-world data and modern topic modeling tools.
