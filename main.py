"""
Main script to integrate and test all modules and run the reminder system.
"""

import sys

from study_reminders.student_manager import StudentsManager

from study_reminders.reminder_logger import log_reminder
from study_reminders.reminder_generator import generate_reminder
from study_reminders.reminder_sender import send_reminder

from study_reminders.reminder_scheduler import trigger, schedule_reminders


def main_menu(student_manager: StudentsManager):
    while True:
        print("\nMAIN MENU")
        print("1. Manage students")
        print("2. Run scheduler")
        print("3. Run tests")
        print("4. Exit")

        choice = input("Select an option (1-4 or CTRL-C to Exit):")

        if choice == "1":
            student_menu(student_manager)
        elif choice == "2":
            scheduler_menu(student_manager)
        elif choice == "3":
            run_tests()
        elif choice == "4":
            sys.exit(0)


def run_tests():
    print("Not implemented.")


def print_students(student_manager: StudentsManager) -> None:
    students = student_manager.get_students()

    for i in range(len(students)):
        student = students[i]
        print(
            f"ID {i} | {student.name} | {student.contact_info} | {student.preferred_time}"
        )


def student_menu(student_manager: StudentsManager):
    while True:
        print("\nMANAGE STUDENTS")
        print("1. Add student")
        print("2. Remove student")
        print("3. List all students")
        print("4. Back to menu")

        choice = input("Select an option (1-4 or CTRL-C to Exit):")

        if choice == "1":
            print("\nADD NEW STUDENT")
            student_name = input("Student name:")
            student_contact_info = input("Student email:")
            student_course = input("Course (e.g. Mathematics):")
            student_preferred_time = input('Preferred time (e.g. "08:00"):')
            student_manager.add_student(
                student_name,
                student_contact_info,
                student_course,
                student_preferred_time,
            )

        elif choice == "2":
            print_students(student_manager) 

            student_id = input("Student ID: ")

            try:
                student = student_manager.remove_student_by_id(int(student_id))
                print(f"Successfully removed {student.name} from the student list.")
            except ValueError:
                print("Wrong value type. Not removing.")

        elif choice == "3":
            print_students(student_manager)
        elif choice == "4":
            print("Returning to menu...")
            break
        else:
            print("Invalid option. Try again.")


def scheduler_menu(student_manager: StudentsManager):
    while True:
        print("\nREMINDER SCHEDULER")
        print("1. Start scheduler")
        print("2. Send reminders manually (for testing)")
        print("3. Back to menu")

        choice = input("Select an option (1-3 or CTRL-C to Exit):")

        if choice == "1":
            schedule_reminders(
                student_manager, generate_reminder, send_reminder, log_reminder
            )
        elif choice == "2":
            trigger(student_manager, generate_reminder, send_reminder, log_reminder)
        elif choice == "3":
            print("Returning to menu...")
            break
        else:
            print("Invalid choice.")


def main():
    student_manager = StudentsManager("students.json")
    main_menu(student_manager)


if __name__ == "__main__":
    main()
