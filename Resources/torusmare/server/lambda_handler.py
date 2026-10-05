"""
Torus Mare - Lambda Handler (Initial Version)
==============================================
This is the server entry point for the Torus Mare exploration game.
For now it only plays the "Gauss number game" to verify connectivity.

Routing approach:
    Since we have a single Lambda behind API Gateway, we use a simple
    dispatch pattern inside the handler rather than a framework. The
    API Gateway sends all POST requests to this one function. We look
    at the request body to decide what to do. No path-based routing
    needed yet — the body content (presence/absence of keys like
    "guess", "PID", "AID") determines the mode and action.

    When we add move/look/admin later, we'll add an "action" key to
    the request body and dispatch on that. Still one Lambda, one handler,
    a few if-branches. Clean and readable.
"""

import json


# The game prompt shown to anonymous users
GAME_PROMPT = 'Welcome! What did Gauss say? Use key "guess=12" if you think he said "12".'

# The correct answer (sum of 1..100, famously computed by young Gauss)
CORRECT_ANSWER = "5050"

# Hardcoded PID for the initial version (will be randomized later)
HARDCODED_PID = "1234567"


def lambda_handler(event, context):
    """
    AWS Lambda entry point.
    
    API Gateway HTTP API sends the request body as a JSON string
    in event["body"]. We parse it, figure out what the user wants,
    and return a JSON response.
    """
    # Parse the request body
    try:
        body = json.loads(event.get("body", "{}") or "{}")
    except (json.JSONDecodeError, TypeError):
        return response(400, {"error_message": "Request body must be valid JSON."})

    # --- Anonymous Mode: Number Guessing Game ---
    # If there's no "guess" key, show the welcome prompt
    if "guess" not in body:
        return response(200, {"message": GAME_PROMPT})

    # There's a guess — let's evaluate it
    guess_value = body["guess"]

    # Convert to string for comparison (handles both "5050" and 5050)
    guess_str = str(guess_value).strip()

    # Check if it's a number at all
    if not guess_str.lstrip("-").isdigit():
        msg = f"oops, that is not a number\n\n{GAME_PROMPT}"
        return response(200, {"message": msg})

    # Check the answer
    if guess_str == CORRECT_ANSWER:
        msg = (
            f"you solved it, nice job, welcome to torusmare, "
            f"your player ID is {HARDCODED_PID}"
        )
        return response(200, {"message": msg, "PID": HARDCODED_PID})

    # Wrong number — give a nudge
    guess_int = int(guess_str)
    correct_int = int(CORRECT_ANSWER)

    if guess_int < correct_int:
        nudge = "too low"
    else:
        nudge = "too high"

    msg = f"{nudge}\n\n{GAME_PROMPT}"
    return response(200, {"message": msg})


def response(status_code, body_dict):
    """Helper to build a properly formatted API Gateway response."""
    return {
        "statusCode": status_code,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(body_dict),
    }
