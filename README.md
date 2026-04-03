# Email-Assistant-Agent

# Requirements
* python -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
* Create .env with OPENAI_API_KEY
* python main.py

# Architecture
┌─────────────────────────────────────────────┐
│           INCOMING EMAIL                    │
│  (from Alice, subject, body, etc.)          │
└──────────────────┬──────────────────────────┘
                   ↓
┌─────────────────────────────────────────────┐
│         TRIAGE ROUTER NODE                  │
│  - Formats prompts with user context        │
│  - Calls GPT-4o-mini with Router schema     │
│  - Returns: ignore/notify/respond           │
└──────────┬──────────────────────────────────┘
           │
           ├─ IGNORE ──→ END
           ├─ NOTIFY ──→ END
           └─ RESPOND ──→ ┌─────────────────────────┐
                          │  RESPONSE AGENT NODE    │
                          │  - ReAct agent          │
                          │  - Has access to tools: │
                          │    • write_email        │
                          │    • schedule_meeting   │
                          │    • check_calendar     │
                          │  - Calls GPT-4o         │
                          │  - Generates response   │
                          └────────────┬────────────┘
                                       ↓
                                      END
