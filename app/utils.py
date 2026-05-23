
FAQ_KEYWORDS = {
    "botox": "services",
    "fillers": "services",
    "consultation": "services",
    "booking": "booking",
    "cancel": "cancellation",
    "hours": "hours"
}


def is_in_scope(user_message):

    lowered = user_message.lower()

    for keyword in FAQ_KEYWORDS:
        if keyword in lowered:
            return True

    return False