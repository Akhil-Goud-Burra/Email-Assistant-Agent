"""Memory store configuration."""
from langgraph.store.memory import InMemoryStore

def create_memory_store():
    """Create and configure the memory store."""
    return InMemoryStore(
        index={"embed": "openai:text-embedding-3-small"}
    )

# Default namespace structure
MEMORY_NAMESPACE = (
    "email_assistant",
    "{langgraph_user_id}",
    "collection"
)