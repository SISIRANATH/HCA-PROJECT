
import json
import os

DB_NAME = "escalations.json"
RULES_FILE = "rules.json"

def init_db():
    """Initialize a mock database for storing escalations."""
    if not os.path.exists(DB_NAME):
        with open(DB_NAME, "w") as f:
            json.dump([], f, indent=2)

def add_escalation(user_query, flagged_ai_response, flag_reason, conversation_history):
    """Save escalated queries to the mock database (JSON file)."""
    data = []
    if os.path.exists(DB_NAME):
        with open(DB_NAME, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []

    record = {
        "user_query": user_query,
        "flag_reason": flag_reason,
        "flagged_ai_response": flagged_ai_response,
        "conversation_history": conversation_history
    }
    data.append(record)
    with open(DB_NAME, "w") as f:
        json.dump(data, f, indent=2)
