from flask import Flask
from dotenv import load_dotenv
from os import 

from langchain.chat_models import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize the Flask app
app = Flask(__name__)

# Loading the OpenAI API key
openai_api_key = os.getenv("OPENAI_API_KEY")

# Checking if the API key is loaded
if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set")

# Initialize the OpenAI model
llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)

# Define the route for the home page