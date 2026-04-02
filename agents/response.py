"""Response agent for handling emails that need replies."""

from langgraph.prebuilt import create_react_agent

from config.profile import PROFILE, PROMPT_INSTRUCTIONS
from config.prompts import agent_system_prompt
from tools.email_tools import TOOLS


def create_prompt(state):
    """Create system prompt with profile context."""
    return [
        {
            "role": "system", 
            "content": agent_system_prompt.format(
                instructions=PROMPT_INSTRUCTIONS["agent_instructions"],
                **PROFILE
            )
        }
    ] + state['messages']


def create_response_agent():
    """Create the response agent with tools."""
    agent = create_react_agent(
        "openai:gpt-4o",
        tools=TOOLS,
        prompt=create_prompt,
    )
    return agent