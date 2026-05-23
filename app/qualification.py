questions = [
    "What type of business do you run?",
    "How large is your team?",
    "What tools do you currently use for customer communication?"
]

def run_qualification():

    answers = {}

    for q in questions:
        response = input(f"\nAI: {q}\nCustomer: ")
        answers[q] = response

    return answers