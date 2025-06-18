import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables from .env file
load_dotenv()

google_api_key = os.getenv('GOOGLE_API_KEY')
if not google_api_key:
    raise ValueError('GOOGLE_API_KEY not found in environment variables. Please set it in your .env file.')

llm = ChatGoogleGenerativeAI(model='gemini-1.5-flash', google_api_key=google_api_key)

# Test the LLM with a simple prompt
response = llm.invoke('Hello')
print('Gemini 1.5 Flash LLM response:', response) 