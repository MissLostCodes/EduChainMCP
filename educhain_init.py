from educhain import Educhain, LLMConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv()

gemini_flash = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

config = LLMConfig(custom_model=gemini_flash)
client = Educhain(config)
