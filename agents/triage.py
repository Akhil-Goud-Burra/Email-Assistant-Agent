"""Triage router for email classification."""

from config.profile import PROFILE, PROMPT_INSTRUCTIONS
from config.prompts import triage_system_prompt, triage_user_prompt
from utils.llm import get_router_llm


def triage_email(email: dict) -> dict:
    """
    Classify an email into ignore/notify/respond.
    
    Args:
        email: Dict with keys 'author', 'to', 'subject', 'email_thread'
    
    Returns:
        Dict with 'classification' and 'reasoning'
    """
    # Get the router LLM
    llm_router = get_router_llm()
    
    # Format the system prompt
    system_prompt = triage_system_prompt.format(
        full_name=PROFILE["full_name"],
        name=PROFILE["name"],
        examples=None,
        user_profile_background=PROFILE["user_profile_background"],
        triage_no=PROMPT_INSTRUCTIONS["triage_rules"]["ignore"],
        triage_notify=PROMPT_INSTRUCTIONS["triage_rules"]["notify"],
        triage_email=PROMPT_INSTRUCTIONS["triage_rules"]["respond"],
    )
    
    # Format the user prompt
    user_prompt = triage_user_prompt.format(
        author=email["author"],
        to=email["to"],
        subject=email["subject"],
        email_thread=email["email_thread"],
    )
    
    # Invoke the router
    result = llm_router.invoke([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ])
    
    return {
        "classification": result.classification,
        "reasoning": result.reasoning
    }