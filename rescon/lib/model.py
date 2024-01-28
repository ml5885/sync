from langchain.chat_models import ChatOpenAI
from ..config import server_config

GPT = lambda: ChatOpenAI(openai_api_key=server_config.openai_api_key, model="gpt-4-1106-preview", max_tokens=2048)