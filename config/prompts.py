# User context. AI Agent can behave context-aware.
PROFILE = {
    "name": "John",
    "full_name": "John Doe",
    "user_profile_background": "Senior software engineer leading a team of 5 developers",
}

/* 
It is used to guide the AI Agent's behavior.
It contains rules for Agent's decision-making.
Rules: ignore - useless emails, notify - important but no reply needed, respond - must reply.
*/
PROMPT_INSTRUCTIONS = {
    "triage_rules": {
        "ignore": "Marketing newsletters, spam emails, mass company announcements",
        "notify": "Team member out sick, build system notifications, project status updates",
        "respond": "Direct questions from team members, meeting requests, critical bug reports",
    },
    "agent_instructions": "Use these tools when appropriate to help manage John's tasks efficiently."
}