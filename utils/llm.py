from langchain.chat_models import init_chat_model
from models.schemas import Router


def get_router_llm():
    """Get LLM configured for routing with structured output."""
    llm = init_chat_model("openai:gpt-4o-mini")
    return llm.with_structured_output(Router)
