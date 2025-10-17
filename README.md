# Installation
Clone this repository and install the package locally using `pip`:
```bash
git clone https://github.com/Noxalas/acit4420_student_reminder_assignment.git
cd acit4420_student_reminder_assignment
pip install
```

# Usage
Run the main script to start the interactive interface:
```bash
python main.py
```
You will see a command-line menu like this:
```bash
MAIN MENU
1. Manage students
2. Run scheduler
3. Run tests
4. Exit
```
For more information check [the report](assignment_2_report.pdf) or the module documentation.

# Modules
| Module | Description |
| ------ | ----------- |
| `reminder_generator` | Provides a `generate()` function for the creation of reminders for students. |
| `reminder_logger` | Logs reminder messages with timestamps to a file. |
| `reminder_sender` | Simulates sending reminders by printing them to the console. |
| `reminder_scheduler` | Schedules and runs daily reminders at specified times using the `schedule` package. |
| `student_manager` | Manages student data: load, save, add, remove. |
