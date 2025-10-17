import datetime

"""
Logs reminder messages with timestamps to a file
"""

def log_reminder(student, reminder) -> None:
    """Log the reminder sent to a student"""
    with open("reminder_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {student['name']}: {reminder}\n")
