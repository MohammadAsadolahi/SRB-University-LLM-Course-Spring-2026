# Practical LLM Course — 9-Session Curriculum

## Target Audience
Master students with medium programming proficiency. Each session is **40 minutes** of hands-on coding using the **OpenAI API** (Chat Completions, Embeddings, Function Calling).

---

## Session 1: LLM API Fundamentals
**Objective:** Set up the OpenAI Python client and understand the core Chat Completions API.
- Installing the `openai` package
- API key configuration
- First chat completion request
- Understanding message roles: `system`, `user`, `assistant`
- Key parameters: `temperature`, `max_tokens`, `top_p`
- Streaming responses
- **Exercise:** Build a simple language translator

---

## Session 2: Prompt Engineering in Practice
**Objective:** Master practical prompting techniques that improve LLM output quality.
- Zero-shot prompting
- Few-shot prompting (1-shot, multi-shot)
- Chain-of-Thought (CoT) prompting
- System prompt design patterns
- Prompt templates with Python f-strings
- **Exercise:** Build a sentiment analyzer with different prompting strategies

---

## Session 3: Structured Outputs & Output Parsing
**Objective:** Extract structured data from LLMs reliably using JSON mode and schemas.
- JSON mode (`response_format: json_object`)
- Structured outputs with `json_schema`
- Parsing and validating LLM outputs
- Error handling for malformed outputs
- **Exercise:** Build a resume/CV information extractor

---

## Session 4: Text Embeddings & Semantic Search
**Objective:** Understand embeddings and build a semantic search engine.
- What are text embeddings?
- OpenAI Embeddings API (`text-embedding-3-small`)
- Cosine similarity computation
- Building a semantic search system over documents
- **Exercise:** Search a FAQ knowledge base

---

## Session 5: Retrieval-Augmented Generation (RAG)
**Objective:** Build a complete RAG pipeline to answer questions from custom documents.
- RAG architecture overview
- Document chunking strategies
- Embedding and indexing documents
- Retrieval + generation pipeline
- **Exercise:** Q&A chatbot over a custom document set

---

## Session 6: Function Calling & Tool Use
**Objective:** Enable LLMs to call external functions and use tools.
- What is function calling?
- Defining tool schemas
- Handling function call responses
- Multi-tool scenarios
- **Exercise:** Build an assistant with calculator and weather tools

---

## Session 7: Building LLM Agents
**Objective:** Build an autonomous agent that reasons and acts using tools in a loop.
- What is an LLM agent?
- The agent loop (Observe → Think → Act)
- ReAct-style reasoning
- Conversation memory
- **Exercise:** Build a research agent that can search and calculate

---

## Session 8: LLM Application Patterns & Best Practices
**Objective:** Learn production patterns for robust LLM applications.
- Chaining multiple LLM calls
- Input guardrails and safety
- Token counting and cost management
- Basic LLM output evaluation
- **Exercise:** Build a moderated content pipeline

---

## Session 9: Capstone — Full LLM Application
**Objective:** Combine all concepts into a complete, functional LLM application.
- Architecture review: RAG + Tools + Agent
- Building a knowledge-base powered assistant
- Adding tools (search, calculator)
- Interactive conversation loop
- Course recap and next steps
- **Exercise:** Extend the assistant with a new tool or knowledge source
