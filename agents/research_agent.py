# agents/research_agent.py - works with langchain 0.3+ / langgraph
from langchain_core.tools import Tool
from langchain_core.messages import HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_agent

from utils.llm import get_llm
from tools.web_search import web_search
from tools.summarizer import summarize
from rag.vector_store import retrieve_docs

llm = get_llm()

tools = [
    Tool(
        name="WebSearch",
        func=web_search,
        description="Search the web for research information. Input should be a search query string."
    ),
    Tool(
        name="Retriever",
        func=retrieve_docs,
        description="Retrieve stored documents from the vector store. Input should be a query string."
    ),
    Tool(
        name="Summarizer",
        func=summarize,
        description="Summarize research text. Input should be the text you want summarized."
    )
]

# LangGraph's create_react_agent - no AgentExecutor needed
agent = create_agent(llm, tools=tools)

def run_agent(query: str) -> str:
    """Run the research agent with a given query."""
    result = agent.invoke({
        "messages": [HumanMessage(content=query)]
    })
    # Extract the last AI message as the final answer
    return result["messages"][-1].content