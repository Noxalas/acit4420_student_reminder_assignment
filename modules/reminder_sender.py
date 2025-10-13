def send_reminder(email: str, reminder: str) -> None:
    if not email:
        raise ValueError("Email address is missing!")
    print(f"Sending reminter to {email}: {reminder}")
