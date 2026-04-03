"""Main entry point for the email assistant."""
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

from config.profile import PROFILE
from config.memory import create_memory_store  # Import memory store
from tests.test_email_samples import COLLEAGUE_QUESTION, MARKETING_EMAIL, SICK_NOTIFICATION
from graph.email_agent import create_email_agent


def show_graph(store):
    """Quick graph visualization."""
    agent = create_email_agent(store)
    
    try:
        with open("graph.png", "wb") as f:
            f.write(agent.get_graph(xray=True).draw_mermaid_png())
        print("✅ Graph saved: graph.png")
    except Exception:
        print(agent.get_graph(xray=True).draw_ascii())


def test_langgraph_workflow():
    """Test the complete LangGraph workflow with memory."""
    print("="*60)
    print("🤖 LANGGRAPH EMAIL AGENT WORKFLOW WITH MEMORY")
    print("="*60)
    print(f"\n👤 Assistant for: {PROFILE['full_name']}")
    print(f"📋 Background: {PROFILE['user_profile_background']}\n")
    
    # Create memory store
    print("🧠 Initializing memory store...")
    store = create_memory_store()
    
    # Create the email agent graph with memory
    print("🔧 Building email agent graph...")
    email_agent = create_email_agent(store)
    print("✅ Graph compiled successfully!\n")

    # Configuration with user ID
    config = {"configurable": {"langgraph_user_id": "john_doe"}}

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
        
        # Invoke the graph with config
        response = email_agent.invoke({"email_input": email}, config=config)
        
        # Display messages if any were generated
        if 'messages' in response and response['messages']:
            print("\n📬 Agent Messages:")
            print("-" * 60)
            for m in response["messages"]:
                m.pretty_print()
        else:
            print("✅ Email processed. No response generated.\n")
        
        print()
    
    # Show stored memories
    print("\n" + "="*60)
    print("🧠 STORED MEMORIES")
    print("="*60)
    namespaces = store.list_namespaces()
    print(f"Namespaces: {namespaces}")
    
    if namespaces:
        memories = store.search(('email_assistant', 'john_doe', 'collection'))
        print(f"\nTotal memories stored: {len(memories)}")
        for i, memory in enumerate(memories, 1):
            print(f"\n--- Memory {i} ---")
            print(memory)
    
    # Add follow-up test after the initial emails are processed
    print("\n" + "="*60)
    print("🔄 TESTING FOLLOW-UP WITH MEMORY")
    print("="*60)

    followup_email = {
        "author": "Alice Smith <alice.smith@company.com>",
        "to": "John Doe <john.doe@company.com>",
        "subject": "Re: Quick question about API documentation",
        "email_thread": """Hi John,

Can you recall the previous email I sent you?

Thanks,
Alice"""
    }

    print(f"From: {followup_email['author']}")
    print(f"Subject: {followup_email['subject']}")
    print()

    response = email_agent.invoke({"email_input": followup_email}, config=config)

    if 'messages' in response and response['messages']:
        print("\n📬 Agent Response:")
        print("-" * 60)
        for m in response["messages"]:
            m.pretty_print()


def main():
    """Run the email agent tests."""
    # Create store once
    store = create_memory_store()
    
    show_graph(store)
    
    # Run the main workflow test
    test_langgraph_workflow()
    
    print("="*60)
    print("✅ All workflows complete!")
    print("="*60)


if __name__ == "__main__":
    main()