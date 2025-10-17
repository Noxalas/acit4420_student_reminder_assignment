"""
Simulates sending reminders by printing them to the console
"""

def send_reminder(email: str, reminder: str) -> None:
    if not email:
        raise ValueError("Email address is missing!")
    print(f"Sending reminder to {email}: {reminder}")
