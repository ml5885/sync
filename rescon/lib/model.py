from langchain.chat_models import ChatOpenAI
from ..config import server_config

GPT = ChatOpenAI(openai_api_key=server_config.openai_api_key, model="gpt-3.5-turbo")