import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(".env"))

class Config():

    openai_api_key = os.getenv("OPENAI_API_KEY")

server_config = Config()