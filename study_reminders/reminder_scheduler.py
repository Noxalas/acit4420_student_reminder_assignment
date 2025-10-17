"""
Schedules and runs daily reminders using the 'schedule' library.
"""

import schedule
import time


def schedule_reminders(students_manager, reminder_generator, reminder_sender, logger):
    """Runs the scheduler to trigger sending reminders to students at their preferred time."""
    for student in students_manager.get_students():

        def job(s=student):
            reminder = reminder_generator(s.name, s.course)
            reminder_sender(s.contact_info, reminder)
            logger({'name': s.name}, reminder)

        schedule.every().day.at(student.preferred_time, "Europe/Amsterdam").do(job)

    print("Scheduler started. Press Ctrl+C to stop.")
    while True:
        schedule.run_pending()
        time.sleep(60)


def trigger(students_manager, reminder_generator, reminder_sender, logger):
    """Manual trigger for sending all reminders immediately for testing."""
    for student in students_manager.get_students():
        reminder = reminder_generator(student.name, student.course)
        reminder_sender(student.contact_info, reminder)
        logger({"name": student.name}, reminder)
