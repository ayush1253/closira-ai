from sop_loader import load_sop
from workflow import ask_ai
from escalation import should_escalate
from qualification import run_qualification
from summarizer import generate_summary
from utils import is_in_scope

# Load SOP
sop = load_sop()

print("AI Support Agent Started")
print("-------------------------")

# Lead qualification
lead_data = run_qualification()

print("\nQualification Complete")
print(lead_data)

conversation_history = []

# Main chat loop
while True:

    user_input = input("\nCustomer: ")

    # Exit condition
    if user_input.lower() == "exit":
        break

    # Rule-based escalation
    escalate, reason = should_escalate(user_input)

    if escalate:

        print(f"\n[ESCALATED TO HUMAN] Reason: {reason}")

        conversation_history.append(f"Customer: {user_input}")
        conversation_history.append(f"ESCALATED: {reason}")

        continue

    # SOP scope check
    if not is_in_scope(user_input):

        print("\nAI:")
        print("I do not have information about that in the current SOP.")

        print("\n[ESCALATED] Reason: Out of SOP scope")

        conversation_history.append(f"Customer: {user_input}")
        conversation_history.append("ESCALATED: Out of SOP scope")

        continue

    # AI response
    result = ask_ai(user_input, sop)

    print("\nAI:")
    print(result["answer"])

    # Save history
    conversation_history.append(f"Customer: {user_input}")
    conversation_history.append(f"AI: {result['answer']}")

    # AI escalation
    if result["needs_escalation"]:

        print(f"\n[ESCALATED] Reason: {result['reason']}")

# Generate summary
summary = generate_summary(conversation_history, lead_data)

print("\n")
print(summary)