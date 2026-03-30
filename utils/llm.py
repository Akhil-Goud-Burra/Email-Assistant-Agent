from langchain.chat_models import init_chat_model
from models.schemas import Router


def get_llm(model: str = "openai:gpt-4o-mini"):
    """Initialize and return an LLM instance."""
    return init_chat_model(model)


def get_router_llm():
    """Get LLM configured for routing with structured output."""
    llm = get_llm("openai:gpt-4o-mini")
    return llm.with_structured_output(Router)