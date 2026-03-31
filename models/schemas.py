"""Pydantic models and type definitions."""

from pydantic import BaseModel, Field
from typing_extensions import TypedDict, Literal, Annotated
from langgraph.graph import add_messages

# 1. class Router(BaseModel): This defines the output format of AI.
# 2. reasoning: str: AI must explain why it made the decision.
# 3. classification: Literal["ignore", "respond", "notify"]: AI must choose ONLY one of these three options.
class Router(BaseModel):
    """Analyze the unread email and route it according to its content."""
    
    reasoning: str = Field(
        description="Step-by-step reasoning behind the classification."
    )

    classification: Literal["ignore", "respond", "notify"] = Field(
        description="The classification of an email: 'ignore' for irrelevant emails, "
        "'notify' for important information that doesn't need a response, "
        "'respond' for emails that need a reply",
    )


# class State(TypedDict): This defines the state of the graph.
class State(TypedDict):
    """Graph state definition."""
    email_input: dict
    messages: Annotated[list, add_messages]