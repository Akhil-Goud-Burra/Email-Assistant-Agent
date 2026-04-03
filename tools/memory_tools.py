"""Memory management tools."""
from langmem import create_manage_memory_tool, create_search_memory_tool
from config.memory import MEMORY_NAMESPACE

# Create memory tools
manage_memory_tool = create_manage_memory_tool(namespace=MEMORY_NAMESPACE)
search_memory_tool = create_search_memory_tool(namespace=MEMORY_NAMESPACE)

# Export for use in agent
MEMORY_TOOLS = [manage_memory_tool, search_memory_tool]