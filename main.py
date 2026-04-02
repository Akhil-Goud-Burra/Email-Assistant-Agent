"""Main entry point for the email assistant."""

from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from config.profile import PROFILE
from tests.test_email_samples import COLLEAGUE_QUESTION, MARKETING_EMAIL, SICK_NOTIFICATION
from graph.email_agent import create_email_agent


def show_graph():
    """Quick graph visualization."""
    agent = create_email_agent()
    
    # Try PNG first
    try:
        with open("graph.png", "wb") as f:
            f.write(agent.get_graph(xray=True).draw_mermaid_png())
        print("✅ Graph saved: graph.png")
    except Exception:
        print(agent.get_graph(xray=True).draw_ascii())

def test_langgraph_workflow():
    """Test the complete LangGraph workflow with multiple emails."""
    print("="*60)
    print("🤖 LANGGRAPH EMAIL AGENT WORKFLOW")
    print("="*60)
    print(f"\n👤 Assistant for: {PROFILE['full_name']}")
    print(f"📋 Background: {PROFILE['user_profile_background']}\n")
    
    # Create the email agent graph
    print("🔧 Building email agent graph...")
    email_agent = create_email_agent()
    print("✅ Graph compiled successfully!\n")

    # Test emails
    test_emails = [
        ("Marketing Email", MARKETING_EMAIL),
        ("Colleague Question", COLLEAGUE_QUESTION),
        ("Sick Notification", SICK_NOTIFICATION),
    ]
    
    # Process each email through the graph
    for name, email in test_emails:
        print("="*60)
        print(f"📧 Processing: {name}")
        print("="*60)
        print(f"From: {email['author']}")
        print(f"To: {email['to']}")
        print(f"Subject: {email['subject']}")
        print()
        
        # Invoke the graph
        response = email_agent.invoke({"email_input": email})
        
        # Display messages if any were generated
        if 'messages' in response and response['messages']:
            print("\n📬 Agent Messages:")
            print("-" * 60)
            for m in response["messages"]:
                m.pretty_print()
        else:
            print("✅ Email processed. No response generated.\n")
        
        print()


def test_single_email_detailed():
    """Test a single email with detailed output."""
    print("\n" + "="*60)
    print("🔍 DETAILED SINGLE EMAIL TEST")
    print("="*60)
    
    # Create agent
    email_agent = create_email_agent()
    
    # Use the colleague question
    email = COLLEAGUE_QUESTION
    
    print(f"\n📧 Email Details:")
    print(f"   From: {email['author']}")
    print(f"   To: {email['to']}")
    print(f"   Subject: {email['subject']}")
    print(f"\n📝 Body:")
    print(f"{email['email_thread']}")
    print("\n" + "-"*60)
    print("🤔 Processing through LangGraph workflow...\n")
    
    # Process
    response = email_agent.invoke({"email_input": email})
    
    # Show all messages
    print("\n📬 Complete Message Thread:")
    print("="*60)
    if 'messages' in response and response['messages']:
        for i, m in enumerate(response["messages"], 1):
            print(f"\n--- Message {i} ---")
            m.pretty_print()
    
    print("\n" + "="*60)


def main():
    """Run the email agent tests."""

    show_graph()
    
    # Run the main workflow test
    test_langgraph_workflow()
    
    # Optional: Run detailed single email test
    # test_single_email_detailed()
    
    print("="*60)
    print("✅ All workflows complete!")
    print("="*60)


if __name__ == "__main__":
    main()