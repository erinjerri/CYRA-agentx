from .. import llm  # from __init__.py
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

template = PromptTemplate(
    input_variables=["question"],
    template="You are a productivity agent. Answer this: {question}"
)

chain = LLMChain(llm=llm, prompt=template)

def run_reasoning_agent(user_input):
    return chain.run(user_input)