import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from config.profile import PROFILE, PROMPT_INSTRUCTIONS
from config.prompts import triage_system_prompt, triage_user_prompt
from tests.test_email_samples import COLLEAGUE_QUESTION, MARKETING_EMAIL, SICK_NOTIFICATION
from utils.llm import get_router_llm


def test_triage(email, email_name):
    """Test the triage router with an email."""
    
    print("\n" + "="*60)
    print(f"📧 Testing: {email_name}")
    print("="*60)
    print(f"From: {email['author']}")
    print(f"Subject: {email['subject']}")
    
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
    print("\n🤔 Analyzing...")
    result = llm_router.invoke([
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt},
    ])
    
    # Display results
    classification_emoji = {
        "ignore": "🚫",
        "notify": "🔔",
        "respond": "📧"
    }
    
    emoji = classification_emoji.get(result.classification, "❓")
    print(f"\n{emoji} CLASSIFICATION: {result.classification.upper()}")
    print(f"\n💭 REASONING:")
    print(f"   {result.reasoning}")


def main():
    """Run triage tests on sample emails."""
    
    print("="*60)
    print("🤖 EMAIL ASSISTANT - TRIAGE TESTING")
    print("="*60)
    print(f"\n👤 Assistant for: {PROFILE['full_name']}")
    print(f"📋 Background: {PROFILE['user_profile_background']}")
    
    # Test all sample emails
    test_triage(COLLEAGUE_QUESTION, "Colleague Question")
    test_triage(MARKETING_EMAIL, "Marketing Email")
    test_triage(SICK_NOTIFICATION, "Sick Notification")
    
    print("\n" + "="*60)
    print("✅ Testing complete!")
    print("="*60)


if __name__ == "__main__":
    main()