---
layout: cover
theme: seriph
background: https://cover.sli.dev
title: Welcome to Slidev
info: |
  ## How to Look at Data
  Presentation slides for developers.

  Learn more at [improvingrag.com](https://improvingrag.com)
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true
---

# How to Look at Data

Building Better RAG Through Measurement

<div class="text-xl mt-8 opacity-80">
  Jeff Huber & Jason Liu
</div>

<div class="text-lg mt-4 opacity-60">
  AIE Summit • June 2025
</div>

---

# The Two-Part Journey

<div class="grid grid-cols-2 gap-8 mt-8">

<div class="p-6 bg-blue-50 rounded-lg">

## Part 1: Measure Your Inputs
**Jeff Huber**

<v-clicks>

- Stop guessing, start testing
- Build fast evals on YOUR data
- Make empirical decisions about retrieval

</v-clicks>

</div>

<div class="p-6 bg-green-50 rounded-lg">

## Part 2: Measure Your Outputs
**Jason Liu**

<v-clicks>

- Turn chat logs into insights
- Cluster conversations to find patterns
- Build feedback loops that improve products

</v-clicks>

</div>

</div>

<v-click>

<div class="text-center mt-8 text-xl font-bold text-blue-600">
  You can't manage what you can't measure
</div>

</v-click>

---
src: part1_jeff.md
---


---
src: part2_jason.md
---

---

# Key Takeaways

## Measure Inputs

- **Stop using public benchmarks** - They're generic, overly clean, and LLMs have seen this data
- **Build fast evals on YOUR corpus** - "If this is queried, this document should be returned"
- **Focus on retrieval accuracy first** - Can you find it? Not "LLM as a judge over all your chunks"
- **Use LLMs to generate synthetic queries** - Align models to write representative queries from your documents  

---

# Key Takeaways

## Measure Outputs

- **Extract structure from conversations** - Use LLMs / Code to pull out frustration, errors, tools used, convo length etc.
- **Cluster similar conversations** - Find patterns you can't see manually
- **Compare KPIs per cluster** - Turn metrics into actionable segments

---

## The Systematic Approach

1. **Start small** - Look at every conversation manually when you can
2. **Extract structure** - Pull out frustration, errors, satisfaction scores
3. **Find clusters** - Group similar conversations to reveal patterns
4. **Compare metrics** - Understand which segments perform well/poorly
5. **Build classifiers** - Monitor patterns in real-time
6. **Make decisions** - Build, fix, or ignore based on data

---

# Resources

- **Example notebooks**: [github.com/567-labs/how-to-look-at-data](https://github.com/567-labs/how-to-look-at-data)
- **Fast evals research**: [research.trychroma.com/generative-benchmarking](https://research.trychroma.com/generative-benchmarking)
- **Deep-dive blog**: [improvingrag.com](http://improvingrag.com/)

</div>

<v-click>

<div class="mt-8 text-center">
  <img src="/images/aie-look-at-data-qrcode.png" alt="QR Code" class="w-48 h-48 mx-auto">
  <div class="mt-2 text-sm opacity-60">Scan for resources</div>
</div>

</v-click>

<v-click>

<div class="mt-8 text-center text-xl">
  <div class="font-bold">Questions?</div>
  <div class="mt-2 opacity-80">Jeff Huber & Jason Liu</div>
</div>

</v-click>