import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import create_tool_calling_agent, AgentExecutor
from langchain.prompts import ChatPromptTemplate
from tools import tools
from agent_prompt import AGENT_PROMPT

# Load environment variables
load_dotenv()
google_api_key = os.getenv('GOOGLE_API_KEY')
llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', google_api_key=google_api_key)

def get_agent_executor(city: str, days: int):
    prompt = ChatPromptTemplate.from_template(AGENT_PROMPT)
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    return agent_executor

# Test instantiation (does not run the agent, just checks setup)
if __name__ == "__main__":
    executor = get_agent_executor("Paris", 3)
    print("AgentExecutor created:", executor) 