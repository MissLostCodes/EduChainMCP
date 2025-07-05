from educhain import Educhain, LLMConfig
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import os
import time


# Load the .env file
load_dotenv()

gemini_flash = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

config = LLMConfig(custom_model=gemini_flash)
client = Educhain(config)
from mcp.server.fastmcp import FastMCP


# Initialize MCP server
mcp = FastMCP("Educhain MCP")

# === Tool: Generate MCQs ===
@mcp.tool()
def generate_mcqs(topic: str, num: int = 5) -> dict:
    """Generate multiple choice questions for a given topic"""
    result = client.qna_engine.generate_questions(topic=topic, num=num)
    return result.model_dump()

# === Tool: Generate Lesson Plan ===
@mcp.tool()
def generate_lesson_plan(topic: str) -> dict:
    """Generate a short lesson plan for a given topic"""
   
    plan = client.content_engine.generate_lesson_plan(topic=topic)
    return plan.model_dump()

# === Start the MCP server ===
if __name__ == "__main__":
    print("Educhain MCP server is now running...")
    mcp.run()