"""Response agent for handling emails that need replies."""

from langgraph.prebuilt import create_react_agent

from config.profile import PROFILE, PROMPT_INSTRUCTIONS
from config.prompts import agent_system_prompt # Unused no-memory prompt
from tools.email_tools import TOOLS

# Import memory tools
from config.prompts import agent_system_prompt_memory  # Use memory version
from tools.memory_tools import MEMORY_TOOLS # Import memory tools


def create_prompt(state):
    """Create system prompt with profile context."""
    return [
        {
            "role": "system", 
            "content": agent_system_prompt_memory.format( # Use memory prompt
                instructions=PROMPT_INSTRUCTIONS["agent_instructions"],
                **PROFILE
            )
        }
    ] + state['messages']


def create_response_agent(store): # Accept store parameter to pass memory store
    """Create the response agent with tools."""
    agent = create_react_agent(
        "openai:gpt-4o",
        tools=TOOLS + MEMORY_TOOLS, # Add memory tools to tools list
        prompt=create_prompt,
        store=store, # Pass memory store to agent
    )
    return agent