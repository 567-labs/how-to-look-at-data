---
layout: cover
theme: seriph
background: https://cover.sli.dev
title: Looking at Your Outputs
info: |
  ## Looking at Your Outputs
  Building systems to turn conversation data into product decisions.

  Learn more at [improvingrag.com](https://improvingrag.com)
class: text-center
drawings:
  persist: false
transition: slide-left
mdc: true

---
# Looking at your outputs 

Building systems to turn conversation data into product decisions.

<!--
Alright, thank you Jeff! What Jeff has effectively described is the ability to compute some metric that helps you select a model. Obviously, what's going to happen is you're going to pick the model with the best cost-latency performance trade-offs. You might even find that an open source model might perform 2-3% better, but it might not be worth it because of the infrastructure costs. These are the kinds of trade-offs you're going to make when you build these systems. And now you start building your write application.
-->

---

## From Model Selection to Real Applications

> What Jeff described: computing metrics to select models with the best cost-latency performance trade-offs.

* Open source might perform 2-3% better, but infrastructure costs matter
* These trade-offs guide your system decisions
* **Now let's talk about building your actual application**

<!--
As I suggested before, we talked about inputs. Now let's talk about outputs. So we've selected our model, we've made our trade-offs, now we need to actually build our application and start thinking about what happens when real users interact with it.
-->

---

## The Manual Review Stage

**When you have dozens of queries or hundreds of conversations:**
* Look at every single one manually
* Think very carefully about each interaction
* Only use LLMs if you're not smarter than the language model
* **Commit the time to look at your data yourself**

<!--
If we live in a world where we have a dozen queries - example queries - or a couple hundred conversations, it might be best to look at every single one and think very carefully about them. If you're asking yourself, "Should I use an LLM to help me make these decisions?", only do so if you think that you're not smarter than a language model. And if you think you are, then you owe it to yourself to commit the time to look at your data.
-->

---

## When Scale Hits Reality

As you build a good product and get real users:

* **Too much volume** to review manually
* **Too much detail** in conversations
* **You're not always the expert** who knows what to look for
* **Outputs are hard to scan** - whole long conversations

**But there's still value there.**

<!--  
But as you scale and get real users, if you build a good product, user conversations are going to have way too much detail. There are going to be situations where you're not the expert who knows what to look for and where to look. There's too much volume to go through things manually. The outputs might be really hard to scan. There might be whole long conversations. But there's still gonna be value there.
-->

---

## The Hidden Signal in Conversations

> How many times have you told a language model: "Try again, do it better, fix it"?

* Conversations hold **unfiltered pain points**
* Better than feedback widgets - users already told you everything
* Raw frustration and retry patterns reveal real problems
* **The data is already there in natural language**

<!--
You might want to build thumb-up buttons and a bunch of different feedback mechanisms. But what you'll realize is that the conversations themselves tend to hold unfiltered pain points. How many times have you just told a language model, "Try again, do it better, fix it, fix it?" That's valuable signal right there. The conversations are already telling you what's working and what's not.
-->

---

## Beyond Simple Metrics

**Marketing analogy:** It's one thing to know your ads score 0.5

**But what if we learn:**
* 80% of users are under 35, 20% are over 35
* Younger audience: performing really well  
* Older audience: performing really poorly

**Now you can make decisions:**
* Double down on younger audience?
* Or figure out why 35+ isn't working?

<!--
That's also considered an example from marketing. It's one thing to know how well your ads are doing. Maybe I can say that the ads are doing well, and if we have some kind of metric, maybe it's doing 0.5, so maybe that's what the eval says. Okay, but what now? Someone tells you to make it better. How? What if we came back and said 80% of the population was under 35, 20% was above 35. And we did really well on the younger population, really poorly on the older population. Now we can make a decision. Maybe we say that it's not worth targeting people above 35. Let's just really double down on a younger audience because it's clear that we're doing well. Maybe we can say, "How come we're not doing well on the 35+ segment? 20% is actually an important segment and it's big enough that we should figure out what we're doing wrong." The difference between having one eval and just being able to group by something is the difference between presenting a number and having a hypothesis as to what's going on.
-->

---

## Extract Structure from Chaos

Use LLMs to extract structured data about conversations:

```python
import instructor
import pydantic 

class ConvoSummary(pydantic.BaseModel):
    summary: str 
    is_frustrated: int # between 0-1 
    made_errors: bool
    tools_used: List[str]
    customer_satisfaction: float
    # ... more fields

client = instructor.from_provider("openai/gpt-4.1-mini")
```

**Similar to what Anthropic's Clio did** - extract key metrics:
* Summary of what happened
* Tools used during conversation  
* Error patterns and frustration levels
* Customer satisfaction scores

<!--
And we can do something similar to what Anthropic's Clio did. We can first use an LLM to extract structured data about a conversation. You can think about things like a summary, the tools that are being used, the error it has made, how frustrated the customer is, and all this kind of stuff.
-->

---

## Implementation: From Chaos to Structure

```python
async def extract_convo_summary(convo: str) -> ConvoSummary:
    prompt = f"""Analyze this conversation and extract key information:
    
    <convo>{convo}</convo>
    """
    
    response = await client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        response_model=ConvoSummary
    )
    
    return response
```

**What we've found in practice:**
* Clusters asking for filters that don't exist
* Questions about data sources we don't have access to
* Underperforming segments with low satisfaction

<!--
In the past, doing this kind of analysis, I've found clusters where users are asking for different filters that didn't exist. You can find clusters that say, "Oh wow, this cluster is asking about a relative time filter, and we just don't have that metadata tag." Maybe it's asking questions on a data source we don't have access to in general, or maybe for some subset of our users. For example, customers asking about how to contact certain individuals, and we don't have a contacts tool. Or we can just find underperforming segments where there's low satisfaction.
-->
---

## The Kura Library Approach

```bash
# Install from PyPI
pip install kura
# Or use uv for faster installation  
uv pip install kura
```

**Pipeline steps:**
1. **Summarize** conversations into structured data
2. **Cluster** similar conversations together  
3. **Build hierarchy** of meta-clusters
4. **Compare KPIs** across clusters

<!--
And this is why Ivan and I have built a couple of tools on top of Instructor that we're known for to do this. If we can have tools that can batch extract and summarize conversations, embed them and run clustering models, we can now use language models to merge these clusters in a hierarchical way to uncover new capabilities or features that might need to be developed, invested in, and prioritized.
-->

---

## Step 1: Import and Setup

```python
from kura import (
    summarise_conversations,
    generate_base_clusters_from_conversation_summaries,
    reduce_clusters_from_base_clusters
)
from kura.types import Conversation
from kura.summarisation import SummaryModel
from kura.cluster import ClusterModel
from kura.meta_cluster import MetaClusterModel
import asyncio
```

<!--
So let's walk through the code step by step. First we import all the components we need from kura. The library is designed to be modular - you can use individual pieces or run the whole pipeline. We're importing the main pipeline functions, the data types, and all the model classes we'll need.
-->

---

## Step 2: Load Your Conversations

```python
# Load conversations from Hugging Face dataset
conversations = Conversation.from_hf_dataset(
    "ivanleomk/synthetic-gemini-conversations",
    split="train"
)

# Or load from your own data
# conversations = Conversation.from_json("your_chats.json")
# conversations = Conversation.from_csv("your_data.csv")
```

<!--
You can load conversations from multiple sources. We have a synthetic dataset on Hugging Face that you can use to try this out, but in practice you'll want to load your own chat data. The library supports multiple input formats so you can work with whatever data format you have.
-->

---

## Step 3: Extract Structured Summaries

```python
# Set up the summarization model
summary_model = SummaryModel()

# Generate summaries with structured data
summaries = await summarise_conversations(
    conversations,
    model=summary_model
)

# Each summary contains:
# - Main topics discussed
# - User frustration level (0-1)
# - Errors made by the system
# - Tools used during conversation
# - Overall satisfaction score
```

<!--
This is where we take those messy, long conversations and extract structured information that we can actually work with. The summary model pulls out key information like what the conversation was about, how frustrated the user got, what tools were used, whether the system made errors. This structured data is what we'll use for all our analysis.
-->

---

## Step 4: Generate Base Clusters  

```python
# Set up clustering model
cluster_model = ClusterModel()

# Create initial clusters from summaries
clusters = await generate_base_clusters_from_conversation_summaries(
    summaries,
    model=cluster_model
)

# This groups similar conversations together
# - "Data visualization help"
# - "SEO content requests" 
# - "Authentication problems"
# - etc.
```

<!--
Now we group similar conversations together. The clustering model looks at those structured summaries and finds patterns - conversations about data visualization, SEO content, authentication issues, whatever patterns exist in your data. This gives us our first level of organization.
-->

---

## Step 5: Build Cluster Hierarchy

```python
# Set up meta-clustering with max clusters limit
meta_cluster_model = MetaClusterModel(max_clusters=10)

# Build hierarchy by merging related clusters
meta_clusters = await reduce_clusters_from_base_clusters(
    clusters,
    model=meta_cluster_model
)

# Creates tree structure:
# Technical Support (50 conversations)
# ├── Database Issues (20 conversations)
# └── Authentication Problems (30 conversations)
```

<!--
The base clustering might give you hundreds of small clusters, which is still hard to analyze. The meta-clustering step builds a hierarchy - it groups related clusters together into bigger themes. So you might have "Technical Support" as a parent cluster with "Database Issues" and "Authentication Problems" as children. This gives you the tree structure you saw earlier.
-->

---

## Real Pipeline Results

```
Clusters (1,250 conversations)
╠══ Generate SEO-optimized content (245 conversations)
║   ╠══ SEO-friendly blog posts (85 conversations)  
║   ╚══ SEO-driven marketing content (62 conversations)
╠══ Data analysis and visualization (180 conversations)
║   ╠══ R analysis help (110 conversations)
║   ╚══ Tableau troubleshooting (70 conversations)
╠══ Technical support (320 conversations)
║   ╠══ Database issues (145 conversations)
║   ╚══ Authentication problems (175 conversations)
╠══ Content creation (285 conversations)
║   ╠══ Blog writing assistance (165 conversations)
║   ╚══ Social media content (120 conversations)
╠══ Code development (220 conversations)
║   ╠══ Python programming help (130 conversations)
║   ╚══ JavaScript debugging (90 conversations)
```

**Now you can:** Group by conversation evals, question evals, and start systematic analysis

<!--
Once we have this data in place, you can just start running these group-bys across conversation evals, question evals, and all that good stuff. And start figuring out how to systematically look at your data, come up with hypotheses and do experiments. You can see here we have 190 conversations broken down into meaningful clusters - SEO content generation, data analysis help, different types of user needs that we can now analyze separately.
-->

---

## From Analysis to Action

**The ultimate goal:** Understanding what to do next

* **Run experiments** based on hypotheses
* **Make product changes** to improve performance  
* **Build the right portfolio** of tools, metadata, and data sources

**Key insight:** Often the solution isn't making AI better - it's building the right supporting infrastructure.

<!--
Because at the end of the day, your ability to make progress is going to be a function of the quality of the hypotheses you're going to make and the velocity with which you tackle experimentation. And what you're going to find is that a lot of the solutions isn't going to be about making the AI better, but just building the right portfolio of tools, metadata filters, and data sources to get the job done.
-->

---

## Systematically improving your AI application

1. **Define success metrics** (KPIs and evals)
2. **Cluster conversations** into meaningful segments
3. **Compare KPIs per cluster** to find patterns
4. **Decide: build, fix, or ignore** each segment
5. **Train classifiers** for real-time monitoring
6. **Create dashboards** and alerts
7. **Make data-driven roadmap decisions**

<!--
It turns out if you can define your success metrics or KPIs - some of which will be evals - you can actually start grouping your conversations into clusters and then compare the KPIs per cluster. Afterwards, you can start to think about how do you build new solutions, fix existing problems, or even just start ignoring things. If 2% of the conversations where people ask questions performed really poorly, maybe the solution is just to add a prompt that says "if they ask questions about this topic, tell them you can't work on it." Move on. Once we have a hypothesis on what kind of clusters and segments of our conversation history we want to focus on, we can then train classifiers to label each individual one and monitor them in real-time.
-->

---

## Quality of Hypotheses × Velocity of Experimentation

> Your ability to make progress = Quality of hypotheses × Speed of experiments

**This system gives you:**

* **Better hypotheses** from systematic data analysis
* **Faster experiments** through clear segmentation
* **Continuous feedback** via real-time classification

<!--
We can plot time series over these things, bar charts, you name it. We can then start doing real-time tagging across evals, metrics, latency, satisfaction, or upvotes. We can build dashboards and alerts, and ultimately we can look at this data systematically and figure out what to prioritize. Because once you have the ability to look at the data, derive scores, and find segments, and group by those segments to understand the scores a little bit better, you're looking at data, but what is the ultimate goal? The ultimate goal is to simply understand what to do next - to run experiments, have hypotheses, and make changes to the product to make them better.
-->