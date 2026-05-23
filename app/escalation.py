

ESCALATION_KEYWORDS = {
    "refund": "Refund request",
    "angry": "Angry sentiment detected",
    "terrible": "Negative customer sentiment detected",
    "manager": "Manager requested",
    "human": "Human agent requested",
    "complaint": "Customer complaint detected",
    "frustrated": "Customer frustration detected",
    "lawsuit": "Legal escalation risk"
}


def should_escalate(message):

    lowered = message.lower()

    for keyword, reason in ESCALATION_KEYWORDS.items():

        if keyword in lowered:
            return True, reason

    return False, None