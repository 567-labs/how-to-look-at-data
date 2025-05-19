# Chroma Workshop: Topic Modeling for RAG Systems

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
   - You will need a `GOOGLE_API_KEY` and an `OPENAI_API_KEY` for running this topic modelling proccess. We're using the OpenAI Text-Embedding-3-Small embeddings for clustering and the Gemini-2.0-flash models for summarisation (used by `kura`).

## Notebooks

1. **1. Cluster Conversations**: Understand query patterns in large RAG applications using topic modeling and Kura, with real user queries from the Weights & Biases documentation. This notebook covers data preparation, clustering, and analysis of user query themes.

## About

This repository was created for the **AI Engineering Summit**. It demonstrates practical techniques for analyzing and improving Retrieval-Augmented Generation (RAG) systems using real-world data and modern topic modeling tools.
