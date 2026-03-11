from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_anthropic import ChatAnthropic
import os
from dotenv import load_dotenv
load_dotenv()

def get_llm():
    return  ChatAnthropic(
            model=os.getenv('MODEL_NAME'),
            temperature=float(os.getenv('TEMPERATURE'))
        )
