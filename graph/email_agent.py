"""Main email agent graph definition with LangGraph workflow."""

from langgraph.graph import StateGraph, START, END
from langgraph.types import Command
from typing import Literal

from models.schemas import State
from agents.triage import triage_email
from agents.response import create_response_agent


def triage_router(state: State) -> Command[Literal["response_agent", "__end__"]]:
    """
    Triage node: classify email and route to appropriate handler.

    Returns Command with:
    - goto: "response_agent" if email needs response, END otherwise
    - update: messages to add to state if routing to response_agent
    """
    result = triage_email(state["email_input"])
    classification = result["classification"]

    if classification == "respond":
        print("📧 Classification: RESPOND - This email requires a response")
        goto = "response_agent"
        update = {
            "messages": [
                {
                    "role": "user",
                    "content": f"Respond to the email {state['email_input']}",
                }
            ]
        }
    elif classification == "ignore":
        print("🚫 Classification: IGNORE - This email can be safely ignored")
        update = None
        goto = END
    elif classification == "notify":
        print("🔔 Classification: NOTIFY - This email contains important information")
        update = None
        goto = END
    else:
        raise ValueError(f"Invalid classification: {classification}")

    return Command(goto=goto, update=update)


def create_email_agent(store): # Accept store parameter to pass memory store
    """
    Build and compile the email agent graph.

    Graph structure:
    START -> triage_router -> (response_agent OR END)
    """
    email_agent = StateGraph(State)

    email_agent.add_node("triage_router", triage_router)
    email_agent.add_node("response_agent", create_response_agent(store))

    email_agent.add_edge(START, "triage_router")

    return email_agent.compile(store=store) # Pass memory store to compile graph
