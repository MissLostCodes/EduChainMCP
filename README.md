# EduChainMCP
# 📚 Educhain MCP Integration with Claude (via MCP Protocol)

This repository provides an integration of the [Educhain](https://github.com/satvik314/educhain) Python library with the Claude AI platform using the [Model Context Protocol (MCP)](https://modelcontextprotocol.io). It allows you to use Claude or Claude Studio to generate:
- ✏️ Multiple-choice questions (MCQs)
- 🧠 Structured lesson plans

Powered by **Gemini 1.5 Flash** (via Langchain) and a custom LLM configuration using Educhain's educational toolkit.

---

## 🚀 Features

- ✅ Claude-native MCP integration
- ✅ Uses OpenAI-compatible Claude Inspector & Claude Desktop apps
- ✅ Tool registration with Educhain’s QnA and LessonPlan engines
- ✅ Gemini 1.5 Flash as the backend LLM
- ✅ Easily extensible for more tools

---

## 🧱 Requirements

- Python 3.10 or later
- A Claude-compatible MCP runtime (`uv`)
- A valid **Gemini API Key** from Google
- Educhain PyPI package installed
- Claude Desktop and MCP Inspector installed

## 🛠️ Setup Instructions
.### 1. Create and activate a virtual environment


python -m venv venv
source venv/bin/activate    # For Linux/macOS
venv\Scripts\activate       # For Windows
pip install educhain


### 2.. Add your Gemini API key in .env

GOOGLE_API_KEY=your_actual_gemini_api_key


### 3. Set up and test EduChain with Gemini
### 4. Install MCP
 pip install mcp[cli]

### 5. Write the mcp tools using educhain in main.py 
   tool1 : generate question and answer
   tool2 : generate lesson plan 

### 6.Run and test in MCP inspector 
uv run mcp dev main.py   
![image](https://github.com/user-attachments/assets/31e34174-6621-481b-88fb-3c13a72dce40)

![image](https://github.com/user-attachments/assets/7af815c2-541e-43b6-a5bd-285607a18c43)

### then add tool to claude desktop using command :
uv run mcp install main.py 
![image](https://github.com/user-attachments/assets/c27780b4-9f1d-4fdc-b8db-ad193e1ac891)


## On claude Desktop :
![image](https://github.com/user-attachments/assets/d7932027-cd6f-4dfd-a154-08c6174f5427)
![image](https://github.com/user-attachments/assets/b24ea9b4-5998-495d-b83f-8be27f09cd81)
Then restart claude and we can use our tools easily . 
![image](https://github.com/user-attachments/assets/1e3fe4ae-c6e1-459f-8cb9-60d7eeca681c)
![image](https://github.com/user-attachments/assets/c510e45b-b682-4487-bc63-d97ffba61ee5)


## testing on claude desktop 
![image](https://github.com/user-attachments/assets/b7990b5b-d9be-4528-94e6-b4a4e22578d3)










