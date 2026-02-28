from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_anthropic import ChatAnthropic
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_agent
from tools import search_tool, wiki_tool, save_text_to_file
from langchain.messages import SystemMessage, HumanMessage

load_dotenv()

class ResearchResponse(BaseModel):
    topic: str
    summary: str
    sources: list[str]
    tools_used: list[str]

llm2 = ChatAnthropic(model_name="claude-sonnet-4-5-20250929", temperature=0.2)

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

agent = create_agent(
    model=llm2,
    tools=[search_tool, wiki_tool, save_text_to_file],
    system_prompt=f"""
You are a professional research assistant.

Answer the user's research query.
Use tools when necessary.

Return your final answer strictly in this format:
{parser.get_format_instructions()}

Do not return anything outside this format.
"""
)

query = input("What can I help you research? ")

# Modern LangChain usually returns a string
response_text = agent.invoke({"messages": [{"role": "user", "content": query}]},
    context={"user_role": "expert"})



try:
    structured_response = parser.parse(response_text)
    print("\nStructured Research Output:\n")
    print(structured_response)

except Exception as e:
    print("\n❌ Error parsing response:", e)
    print("Raw response:", response_text)