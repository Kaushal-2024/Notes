# LangChain Components

LangChain provides modular components to build LLM-powered applications. These components work together to create flexible and powerful pipelines for language tasks.

---

## 1. Model Components

### a. Language Models

- **LLMs (Large Language Models)**  
  General-purpose models used for tasks like text generation, summarization, etc.  
  > ⚠️ Considered the "old way" in LangChain — not preferred for conversation-heavy apps.

- **Chat Models**  
  Specialized in conversational tasks with structured message formats (e.g., OpenAI's ChatGPT, Anthropic’s Claude).  
  > ✅ Preferred for new projects focused on dialogue and interactivity.
  
### b. Embedding Models

- Used to convert text into vector representations for semantic search and similarity tasks.  
- Common use cases: document search, retrieval-based QA.  
  > E.g., OpenAI Embeddings, HuggingFace Transformers

---


## 2. Prompt Templates

Prompts define how inputs are structured before being passed to the model. LangChain offers various tools to make prompt engineering modular and reusable.

### Prompt Types

- **Static Prompt**  
  A fixed text prompt — not parameterized.

- **Dynamic Prompt**  
  A flexible prompt that uses placeholders and is filled in at runtime.

---

### Core Classes

- **`PromptTemplate`**  
  A template for building prompts with variables. Useful for LLMs (non-chat models).  
  > Example: `"Translate this text to French: {input_text}"`

- **`ChatPromptTemplate`**  
  Designed for chat-based models. Supports multiple messages with roles (system, user, assistant).

---

### Message Types (for ChatPromptTemplate)

Used to simulate conversational interactions:

- **SystemMessage**  
  Sets the behavior or personality of the assistant.

- **HumanMessage**  
  Represents user input.

- **AIMessage**  
  Represents model responses.

- **MessagePlaceholder**  
  A placeholder for dynamic insertion of message history or content.

> 🧠 These are especially useful when building chat applications that maintain context across turns.

---

### Prompt Patterns

- **Role-Based Prompts**  
  Prompts that clearly assign roles (e.g., system, user, assistant) to guide the model's behavior.

- **Few-Shot Prompts**  
  Include several examples of input-output pairs to help the model generalize the task better.

> 💡 Prompt templates allow for easy experimentation and rapid iteration when fine-tuning model behavior.


---

## **Structured Output**

Structured output helps you extract clean, machine-readable results (like JSON or Python objects) from LLMs — useful for integrating LLM responses into downstream logic or tools.

---

### ✅ Using `with_structured_output()`

This method wraps your model to enforce structured outputs. It includes a `method` parameter with two main options:

1. **`"json"`**
   Forces the model to return output in strict JSON format.

2. **`"function_calling"`**
   Uses OpenAI-style function calling to map model output directly to a function’s schema.

   > 🔧 Useful for tool usage and agents — ensures output conforms to a function’s expected arguments.

---

### 📦 Data Schema Options

To define the expected output structure, LangChain supports:

* **`TypedDict`**
  Basic structure definition using Python typing.
  ⚠️ Only provides shape — does **not** enforce runtime validation.

* **`Pydantic`**
  Strongly recommended for validation and parsing.
  ✅ Supports type checking, default values, and validation.

* **`JSON Schema`**
  For compatibility with external systems or APIs using formal JSON definitions.

> 🧠 Pydantic is typically the best choice for enforcing output formats and handling errors gracefully.

---

Here’s your improved and enhanced **Output Parsers** section with corrected grammar, improved clarity, and a few practical details added for better understanding:

---

### 🧰 Output Parsers

**Output parsers** are used to transform the raw text response from an LLM into structured Python data — especially useful when the model doesn't natively support structured output (like JSON or function calls).

#### ✅ Common Use Cases:

* Converting free-form text into structured data (e.g., `dict`, `list`)
* Parsing answers into formats usable in downstream logic (e.g., decision trees, databases)
* Enabling structured workflows even with plain-text-only models

---

### 🔧 Common Output Parser Classes

| Parser                               | Description                                                                                                 |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------- |
| **`StrOutputParser`**                | Returns plain string output. Simple and useful for chaining in pipelines.                                   |
| **`JSONOutputParser`**               | Extracts JSON from the model's output, but **does not** validate against a schema.                          |
| **`StructuredOutputParser`**         | Returns structured data based on a defined schema (e.g., `TypedDict`), but **does not perform validation**. |
| **`PydanticOutputParser`**           | Parses and **validates** output using Pydantic models. Ideal when data correctness is critical.             |
| **`RegexParser`**                    | Extracts specific patterns from text using regular expressions. Great for narrow, predictable outputs.      |
| **`CommaSeparatedListOutputParser`** | Converts comma-separated text into a Python list. Useful for quick list parsing.                            |





## 3. Chains

Chains connect multiple components (e.g., prompt → model → output parser) into a logical sequence.

- **Sequential Chain**  
  Simple linear pipeline.

- **Parallel Chain**  
  Run multiple chains simultaneously (e.g., for multi-document processing).

- **Conditional Chain**  
  Logic-based branching (e.g., if X, then use Y model).

> 🧠 Chains allow composability for building complex flows.

---

## 4. Indexes (Document Preparation and Retrieval)

Indexes help organize and query documents efficiently.

### a. **Document Loaders**  
Import content from files, web pages, PDFs, databases, etc.

### b. **Text Splitters**  
Break long documents into smaller, manageable chunks.

### c. **Vector Stores**  
Store text embeddings for efficient similarity search.  
> E.g., FAISS, Pinecone, Chroma

### d. **Retrievers**  
Query vector stores and return relevant documents.

> 🔍 Used in Retrieval-Augmented Generation (RAG) pipelines.

---

## 5. Memory

Memory helps maintain conversation context across interactions.

> ⚠️ LLM API calls are stateless by default — memory solves this.

### Types of Memory:

1. **ConversationBufferMemory**  
   Stores the full conversation history.

2. **ConversationBufferWindowMemory**  
   Maintains only the latest _k_ interactions (windowed history).

3. **ConversationSummaryMemory**  
   Summarizes past messages for efficiency in long sessions.

4. **Custom Memory**  
   Define your own memory logic for specialized needs.

> 🧠 Useful for chatbots and multi-turn interactions.

---

## 6. Agents

Agents make decisions and select tools dynamically to solve tasks — like a chatbot with reasoning superpowers.

### Key Features:

- **Tool usage**  
  Agents can call tools like web search, code execution, calculators, etc.

- **Reasoning Abilities**  
  They decide which tool or chain to use based on the user query.

> 🤖 Agents = LLM + Tools + Memory + Logic

---

