from openai import OpenAI
from dotenv import load_dotenv
import os
import json

from prompts import SYSTEM_PROMPT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("GROQ_API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

MODEL = "llama-3.1-8b-instant"

def ask_ai(user_message, sop_data):

    try:

        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": f"""
{SYSTEM_PROMPT}

SOP DATA:
{sop_data}
"""
                },
                {
                    "role": "user",
                    "content": user_message
                }
            ],
            temperature=0.2
        )

        text = response.choices[0].message.content.strip()

        # Remove markdown if present
        text = text.replace("```json", "").replace("```", "").strip()

        # Extract JSON safely
        start = text.find("{")
        end = text.rfind("}") + 1

        json_text = text[start:end]

        return json.loads(json_text)

    except Exception as e:

        return {
            "answer": "I'm unable to process the request right now.",
            "confidence": 0,
            "needs_escalation": True,
            "reason": str(e)
        }