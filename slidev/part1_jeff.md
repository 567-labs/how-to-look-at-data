# The Problem

You can't manage what you can't measure

<v-clicks>

- **Intervention Bias**: "hey guys would this work, would that work?"
- **Why guess when you can test?**
- **Stop flying blind** - without measurement, you'll just thrash and crash

</v-clicks>

<v-click>

<div class="text-center mt-8">
  <div class="text-2xl opacity-75">Word cloud of common problems:</div>
  <div class="mt-4 text-lg opacity-60">Issues • Questions • Guesswork • Uncertainty</div>
</div>

</v-click>

---

# The Solution

Look at your data!

<v-clicks>

- **Great measurement makes systematic improvement easy**
- **Look at your inputs AND outputs**
  - **Inputs**: Build & Test - look at your documents
  - **Outputs**: Deploy & Monitor - look at your logs

</v-clicks>

<v-click>

<div class="text-center mt-8">
  <div class="w-32 h-32 mx-auto border-4 border-blue-400 rounded-full flex items-center justify-center">
    <div class="text-blue-400 font-bold">INPUT → OUTPUT</div>
  </div>
</div>

</v-click>

---

# Inputs: Look at Your Documents

There are many decisions in setting up your retrieval system

<v-clicks>

- **Which chunking strategy?**
- **Which embedding model?**
- **Query expansion?**
- **Reranking?**
- **And many more...**

</v-clicks>

<v-click>

<div class="text-center mt-8 p-4 bg-gray-100 rounded-lg">
  <div class="text-xl font-bold text-red-600">⚠️ Critical Point</div>
  <div class="mt-2">Public benchmarks are NOT representative of your data</div>
</div>

</v-click>

---

# Why Public Benchmarks Fail

<v-clicks>

- **Generic** - not specific to your domain
- **Overly clean** - real data is messy
- **Used for training** - LLMs and embedding models have seen this data

</v-clicks>

<v-click>

<div class="mt-8">
  <img src="/api/placeholder/600/300" alt="Generic benchmark vs Real data comparison" class="mx-auto rounded-lg shadow-lg">
</div>

</v-click>

---

# Fast Evals: The Solution

What is a fast eval?

<v-clicks>

- **"If this is queried, this document should be returned"**
- **A set of these = golden dataset**
- **Focus on "can you find it"**
- **Not "LLM as a judge over all your chunks"**

</v-clicks>

<v-click>

<div class="mt-8 p-4 bg-blue-50 rounded-lg">
  <div class="font-bold text-blue-800">Key Insight:</div>
  <div class="mt-2">Fast evals make decisions easy by focusing on retrieval accuracy</div>
</div>

</v-click>

---

# How Fast Evals Work

Use LLMs to write queries for your documents

<v-clicks>

1. **Take your corpus**
2. **Align an LLM to write representative synthetic queries**
3. **Get a golden dataset**
4. **Run your evals**
5. **Make empirical decisions**

</v-clicks>

<v-click>

<div class="mt-8 text-center">
  <div class="inline-flex items-center space-x-4 text-lg">
    <div class="px-4 py-2 bg-blue-100 rounded">Corpus</div>
    <div>→</div>
    <div class="px-4 py-2 bg-green-100 rounded">Synthetic Queries</div>
    <div>→</div>
    <div class="px-4 py-2 bg-yellow-100 rounded">Golden Dataset</div>
    <div>→</div>
    <div class="px-4 py-2 bg-red-100 rounded">Decisions</div>
  </div>
</div>

</v-click>

---

# Case Study: Weight & Biases Chatbot

Generative benchmarking revealed surprising insights

<v-clicks>

- **Their original embedding model performed worst** out of 4 models tested
- **Contradiction with MTEB model rankings**
- **36% of document chunks were judged irrelevant**

</v-clicks>

<v-click>

<div class="mt-8">
  <img src="/api/placeholder/600/300" alt="W&B model performance comparison" class="mx-auto rounded-lg shadow-lg">
</div>

</v-click>

---

# Case Study Results

<div class="grid grid-cols-2 gap-8">

<div>

## Model Performance
<img src="/api/placeholder/400/300" alt="Model performance chart" class="rounded-lg shadow-lg">

</div>

<div>

## Document Relevance
<img src="/api/placeholder/400/300" alt="Document relevance analysis" class="rounded-lg shadow-lg">

</div>

</div>

<v-click>

<div class="mt-8 text-center">
  <a href="https://research.trychroma.com/generative-benchmarking" target="_blank" class="text-blue-400 hover:text-blue-300">
    📱 QR Code: research.trychroma.com/generative-benchmarking
  </a>
</div>

</v-click>