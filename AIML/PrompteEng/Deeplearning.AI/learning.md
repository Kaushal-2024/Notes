## 🔧 General Prompting Principles (`l2-guidelines.ipynb`)
- Be **clear** and **specific**.
- Ask for the **desired format** (JSON, list, paragraph).
- Break complex tasks into smaller ones.
- Use **few-shot examples** for better accuracy.

**Example Prompts:**
```text
Summarize the paragraph in one sentence.
Convert this email to a more formal tone.
```

---

## 🔁 Iterative Prompt Development (`l3-iterative-prompt-development.ipynb`)
- Start simple, then **refine** based on results.
- Improve prompt quality step by step (like debugging).
- Think in terms of versioning your prompt.

**Example Progression:**
```text
1. Fix grammar in this sentence.
2. Fix grammar and return only the corrected sentence.
3. Fix grammar, spelling, and awkward phrasing. Return plain text.
```

---

## 📝 Summarizing Text (`l4-summarizing.ipynb`)
- Use prompts to **shorten** or **reformat** content.
- Tailor summaries: bullet points, headlines, TL;DR, etc.

**Example Prompts:**
```text
Summarize this article in bullet points.
Give an executive summary of this report.
```

---

## 🔍 Inferring Information (`l5-inferring.ipynb`)
- Extract **meaning, categories, or emotions** from text.
- Common tasks: classification, sentiment, intent detection.

**Example Prompts:**
```text
What is the sentiment of this review?
What language is this paragraph written in?
```

---

## 🔄 Transforming Content (`l6-transforming.ipynb`)
- Change the **style, tone, or format** of text.
- Useful for localization, tone shift, formal/casual rewrite, etc.

**Example Prompts:**
```text
Translate this to French in a formal tone.
Rewrite this message to sound more professional.
```

---

## ➕ Expanding Ideas (`l7-expanding.ipynb`)
- Take short inputs and generate longer, richer content.
- Great for content generation, SEO, product descriptions.

**Example Prompts:**
```text
Expand this bullet point into a full paragraph.
Write a blog intro based on this topic.
```

---

## 🤖 Building a Chatbot (`l8-chatbot.ipynb`)
- Learn role-based prompting with `system`, `user`, `assistant`.
- Control assistant behavior via system instructions.
- Supports multi-turn conversation context.

**Example Structure:**
```json
[
  {"role": "system", "content": "You are a helpful coding assistant."},
  {"role": "user", "content": "How do I create a FastAPI project?"}
]
```

