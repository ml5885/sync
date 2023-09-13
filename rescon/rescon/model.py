from langchain.chat_models import ChatOpenAI
from ..config import OPENAI_API_KEY

GPT = ChatOpenAI(openai_api_key=OPENAI_API_KEY, model="gpt-4")