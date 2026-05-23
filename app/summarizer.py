def generate_summary(conversation, lead_data):

    summary = f"""
========================
CONVERSATION SUMMARY
========================

Customer Intent:
Asked about clinic services and pricing.

Lead Qualification:
"""

    for question, answer in lead_data.items():
        summary += f"- {question}: {answer}\n"

    summary += """

Conversation History:
"""

    for item in conversation:
        summary += f"{item}\n"

    summary += """

Recommended Action:
- Human follow-up for unresolved queries.
"""

    return summary