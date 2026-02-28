---

# 🧠 Research Agentic AI

An AI-powered research assistant built with **LangChain**, **Anthropic Claude**, and **Pydantic** that generates structured research outputs using external tools like web search and Wikipedia.

This project demonstrates:

* Tool-augmented AI agents
* Structured output parsing
* Error handling for LLM responses
* Clean modular architecture

---

## 🚀 Features

* 🔎 Web search integration
* 📚 Wikipedia lookup
* 💾 Save research results to file
* 🧾 Strict structured output using Pydantic
* 🤖 Powered by Claude (Anthropic)
* 🛡️ Output validation with parser fallback

---

## 🏗️ Tech Stack

* Python 3.10+
* LangChain
* Anthropic Claude (via `langchain_anthropic`)
* Pydantic
* python-dotenv

---

## 📂 Project Structure

```
.
├── main.py
├── tools.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/research-agentic-ai.git
cd research-agentic-ai
```

### 2️⃣ Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate  # Mac/Linux
.venv\Scripts\activate     # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory:

```
ANTHROPIC_API_KEY=your_anthropic_api_key_here
```

---

## 🧠 How It Works

1. User enters a research query.
2. The LangChain agent decides which tools to use:

   * Search tool
   * Wikipedia tool
   * File-saving tool
3. Claude generates a structured response.
4. `PydanticOutputParser` validates the output.
5. If parsing fails, raw output is displayed for debugging.

---

## 📌 Structured Output Format

The agent strictly returns:

```python
class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]
```

This ensures:

* Clean data
* Type safety
* Production-ready responses

---

## ▶️ Usage

Run:

```bash
python main.py
```

Then enter your research topic:

```
What can I help you research? causes of cancer
```

Example output:

```
Structured Research Output:

topic='Causes of Cancer'
summary='Cancer is caused by genetic mutations...'
sources=['https://example.com']
tools_used=['search_tool', 'wiki_tool']
```

---

## 🛠️ Example Use Cases

* Academic research assistant
* Blog content research automation
* Technical documentation helper
* Market research summarization
* AI-powered CLI research tool

---

## 📈 Future Improvements

* Add streaming responses
* Add memory support
* Convert to FastAPI backend
* Add frontend UI (React / Next.js)
* Add multi-model support (OpenAI, DeepSeek, etc.)

---

## 📜 License

MIT License

---

## 🙌 Author

Built by **Victor Adeniyi**
AI Engineer | Software Developer

---
