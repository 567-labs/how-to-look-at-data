---
theme: seriph
background: https://cover.sli.dev
title: How to Look at Data
info: |
  ## How to Look at Data
  Systematically Improving RAG Applications
  
  Learn more at [trychroma.com](https://trychroma.com) and [improvingrag.com](https://improvingrag.com)
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# How to Look at Data

Systematically Improving RAG Applications

<div class="pt-12">
  <span @click="$slidev.nav.next" class="px-2 py-1 rounded cursor-pointer" hover:bg="white op-10">
    Press Space for next page <carbon:arrow-right class="inline"/>
  </span>
</div>

<div class="abs-br m-6 flex gap-2">
  <button @click="$slidev.nav.openInEditor()" title="Open in Editor" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:edit />
  </button>
  <a href="https://github.com/567-labs/how-to-look-at-data" target="_blank" alt="GitHub" title="Open in GitHub" class="text-xl slidev-icon-btn opacity-50 !border-none !hover:text-white">
    <carbon:logo-github />
  </a>
</div>

---

# The Problem

Most RAG systems fail because we don't understand our data

<v-clicks>

- 🔍 **Blind optimization** - tweaking without understanding patterns
- 📊 **No visibility** - can't see what users actually ask
- 🎯 **Generic solutions** - one-size-fits-all approaches
- 🔧 **Intervention bias** - constantly tweaking models/prompts to feel productive
- 👻 **Absence blindness** - can't fix retrieval problems we don't measure

</v-clicks>

<v-click>

**Solution**: Look at your data systematically

</v-click>

---

# Why You Need a System

Without a system, teams face predictable challenges

<v-clicks>

- 😰 **"Make the AI better"** → Anxiety and guesswork
- 🎲 **Resource allocation** → Political decisions vs data-driven
- 🤔 **Evaluating ideas** → Subjective opinions vs objective measurement
- 📢 **Communicating progress** → Vague assertions vs concrete metrics
- 🚨 **User complaints** → Reactive firefighting vs proactive improvement

</v-clicks>

<v-click>

**A system frees up mental energy for innovation**

</v-click>

---

# What a System Means for Your Team

<div class="grid grid-cols-2 gap-8">

<div>

## Without System
- Debates about what *might* work
- Anxiety when asked to improve
- Unclear priorities and tradeoffs
- Subjective performance assessment
- Ad-hoc problem solving

</div>

<div>

## With System
- Focus on testing hypotheses
- Confidence in improvement paths
- Data-driven prioritization
- Objective metrics and benchmarks
- Structured problem solving

</div>

</div>

---

# What a System Means for Your Process

<v-clicks>

- 📋 **Framework** for evaluating technologies
- 🎯 **Decision process** for prioritizing development efforts  
- 🔧 **Methodology** for diagnosing and improving performance
- 📊 **Standard metrics** and benchmarks for measuring success
- 🔄 **Feedback loops** that turn user interactions into improvements

</v-clicks>

<v-click>

**Result**: Less guesswork, more confidence in every decision

</v-click>

---

---

# The Approach

<v-clicks>

1. **Cluster conversations** - find query patterns
2. **Better summaries** - actionable insights, not generic labels  
3. **Build classifiers** - monitor topics in production

</v-clicks>

<v-click>

**Real data**: 560 W&B documentation conversations

</v-click>

---

# Topic Modeling with Kura

```python
from kura import Kura
import chromadb

# Cluster user queries
kura = Kura()
topics = kura.cluster(conversations, n_clusters=8)
```

<v-click>

**Result**: Clear patterns in what users actually care about

</v-click>

---
layout: center
class: text-center
---

# Live Demo

Let's analyze the data

<div class="text-6xl text-blue-400 mb-4">
  🔍
</div>

---

# Production Monitoring

```python
# Train classifier from discovered topics
classifier.fit(embeddings, topic_labels)

# Monitor in production
topic, confidence = classify_query(new_query)
if confidence < 0.7:
    flag_for_review(new_query)
```

---
layout: center
class: text-center
---

# Resources

<div class="mt-8 flex justify-center gap-8">
  <a href="https://trychroma.com" target="_blank" class="text-blue-400">
    trychroma.com
  </a>
  <span class="opacity-50">•</span>
  <a href="https://improvingrag.com" target="_blank" class="text-blue-400">
    improvingrag.com
  </a>
</div>

<div class="mt-8 text-sm opacity-75">
  github.com/567-labs/how-to-look-at-data
</div>

---
layout: center
class: text-center
---

# Thank You

Start looking at your data systematically

<div class="mt-8 flex justify-center gap-8">
  <a href="https://trychroma.com" target="_blank" class="text-blue-400 hover:text-blue-300">
    trychroma.com
  </a>
  <span class="opacity-50">•</span>
  <a href="https://improvingrag.com" target="_blank" class="text-blue-400 hover:text-blue-300">
    improvingrag.com
  </a>
  <span class="opacity-50">•</span>
  <a href="https://github.com/567-labs/how-to-look-at-data" target="_blank" class="text-blue-400 hover:text-blue-300">
    GitHub
  </a>
</div>

<div class="mt-12 text-sm opacity-75">
  AI Engineering Summit 2024
</div>

<!--
Thank you for attending! Remember: the key to better RAG systems is understanding your data systematically, not just tweaking parameters blindly.
--> 