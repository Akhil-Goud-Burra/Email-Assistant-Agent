import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from config.prompts import PROFILE, PROMPT_INSTRUCTIONS
from tests.test_email_samples import COLLEAGUE_QUESTION
from utils.llm import get_router_llm


def test_router():
    """Test the email router with a sample email."""
    
    print("="*60)
    print("TESTING EMAIL ROUTER")
    print("="*60)
    
    # Get the router LLM
    llm_router = get_router_llm()
    
    # Create a simple prompt
    email = COLLEAGUE_QUESTION
    prompt = f"""
Classify this email:

From: {email['author']}
Subject: {email['subject']}
Body: {email['email_thread']}

Rules:
- IGNORE: Marketing newsletters, spam
- NOTIFY: Important info, no response needed
- RESPOND: Direct questions, meeting requests
"""
    
    # Test the router
    print(f"\nEmail from: {email['author']}")
    print(f"Subject: {email['subject']}")
    print("\n Analyzing...")
    
    result = llm_router.invoke(prompt)
    
    print(f"\n RESULT:")
    print(f"  Classification: {result.classification.upper()}")
    print(f"  Reasoning: {result.reasoning}")
    

def main():
    """Run tests."""
    test_router()


if __name__ == "__main__":
    main()