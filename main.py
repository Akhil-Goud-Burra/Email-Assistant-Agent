# Import your config
from config.prompts import PROFILE, PROMPT_INSTRUCTIONS
from tests.test_email_samples import COLLEAGUE_QUESTION

def main():    
    print("="*60)
    print("📋 EMAIL ASSISTANT CONFIGURATION")
    print("="*60)
    
    print("\n👤 PROFILE:")
    print(f"  Name: {PROFILE['name']}")
    print(f"  Full Name: {PROFILE['full_name']}")
    print(f"  Background: {PROFILE['user_profile_background']}")
    
    print("\n📜 TRIAGE RULES:")
    print(f"  Ignore: {PROMPT_INSTRUCTIONS['triage_rules']['ignore']}")
    print(f"  Notify: {PROMPT_INSTRUCTIONS['triage_rules']['notify']}")
    print(f"  Respond: {PROMPT_INSTRUCTIONS['triage_rules']['respond']}")
    
    print("\n" + "="*60)
    print("📧 TEST EMAIL")
    print("="*60)
    print(f"From: {COLLEAGUE_QUESTION['author']}")
    print(f"To: {COLLEAGUE_QUESTION['to']}")
    print(f"Subject: {COLLEAGUE_QUESTION['subject']}")
    print(f"\nBody:\n{COLLEAGUE_QUESTION['email_thread']}")
    
    print("\n✅ Configuration loaded successfully!")

if __name__ == "__main__":
    main()