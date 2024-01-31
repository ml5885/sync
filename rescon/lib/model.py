from langchain.chat_models import ChatOpenAI

def GPT(api_key):
    return ChatOpenAI(
        openai_api_key=api_key,
        model="gpt-4-1106-preview",
        max_tokens=2048
    )