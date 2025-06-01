from langchain.agents import initialize_agent
from langchain.llms import OpenAI
from langchain.tools import Tool

def summarize(text):
    return f"Summary: {text}"

llm = OpenAI()
tools = [
    Tool(name="Summarize", func=summarize, description="Summarize the transcribed input.")
]

def run_lang_agent(result_text):
    agent = initialize_agent(tools, llm, agent="zero-shot-react-description")
    return agent.run(result_text)