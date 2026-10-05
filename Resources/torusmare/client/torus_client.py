"""
Torus Mare - Client Helper
===========================
Student-facing helper functions for talking to the Torus Mare server.
Uses the Python 'requests' library exclusively.

Usage:
    from torus_client import guess

    # See the welcome message
    result = guess()
    print(result["message"])

    # Submit a guess
    result = guess(42)
    print(result["message"])
"""

import requests

# The server URL
SERVER_URL = "https://j2m1oh7g1d.execute-api.us-west-2.amazonaws.com"

# Timeout for all requests (seconds)
TIMEOUT = 10


def guess(value=None):
    """
    Play the number guessing game.

    Call with no argument to see the welcome prompt.
    Call with an integer to submit a guess.

    Returns the server response as a Python dictionary.
    """
    body = {}
    if value is not None:
        body["guess"] = str(value)

    try:
        resp = requests.post(SERVER_URL, json=body, timeout=TIMEOUT)
    except requests.exceptions.ConnectionError:
        print("connection error: could not reach the server for guess action")
        return None
    except requests.exceptions.Timeout:
        print("connection error: server did not respond in time for guess action")
        return None

    # Check for error responses
    if resp.status_code in (400, 404):
        data = resp.json()
        print(data.get("error_message", "Unknown error from server"))
        return data

    return resp.json()
