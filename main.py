"""
main.py

Entry point. Run this file: `python main.py`

It loops through the test messages, sends each one to Neuro via
client.ask_neuro(), and prints the conversation.
"""

from client import ask_neuro

if __name__ == "__main__":
    for i, msg in enumerate(TEST_MESSAGES, start=1):
        print(f"\n--- Test {i} ---")
        print(f"User: {msg}")
        reply = ask_neuro(msg)
        print(f"Neuro: {reply}")
