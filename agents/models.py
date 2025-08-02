import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")

llm_gemini_flash = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    api_key=gemini_api_key,
    temperature=0.6,
)

llm_gemini_pro = ChatGoogleGenerativeAI(
    model="gemini-2.5-pro",
    api_key=gemini_api_key,
    temperature=1,
)

