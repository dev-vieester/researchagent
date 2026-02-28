from langchain_community.tools import WikipediaQueryRun, DuckDuckGoSearchRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain.tools import tool
from datetime import datetime


# -----------------------------
# 1️⃣ Save Tool (Custom Tool)
# -----------------------------
@tool
def save_text_to_file(data: str) -> str:
    """
    Saves structured research data to a text file.
    Use this tool when you want to persist final research output.
    """
    filename = "research_output.txt"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    formatted_text = (
        f"--- Research Output ---\n"
        f"Timestamp: {timestamp}\n\n"
        f"{data}\n\n"
    )

    with open(filename, "a", encoding="utf-8") as f:
        f.write(formatted_text)

    return f"Data successfully saved to {filename}"


# -----------------------------
# 2️⃣ DuckDuckGo Search Tool
# -----------------------------
search_tool = DuckDuckGoSearchRun()


# -----------------------------
# 3️⃣ Wikipedia Tool
# -----------------------------
api_wrapper = WikipediaAPIWrapper(
    top_k_results=1,
    doc_content_chars_max=500
)

wiki_tool = WikipediaQueryRun(api_wrapper=api_wrapper)


# -----------------------------
# 4️⃣ Export Tools List
# -----------------------------
tools = [
    search_tool,
    wiki_tool,
    save_text_to_file
]