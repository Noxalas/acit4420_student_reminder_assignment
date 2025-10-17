"""
Manages student data: load, save, add, remove, list.
"""

from dataclasses import dataclass, asdict
from typing import List, Dict, Any
import json


@dataclass
class Student:
    """Data class for student data."""

    name: str 
    contact_info: str # Email 
    course: str
    preferred_time: str # e.g., "14:00" 


class StudentsManager:
    def __init__(self, file_path="students.json"):
        self.file_path = file_path
        self.students: List[Student] = self.load_students(file_path)


    @staticmethod
    def load_students(file_path) -> 'List[Student]':
        """Loads the student list from a JSON file in a file path."""
        try:
            with open(file_path, "r") as file:
                data = json.load(file)
                return [Student(**item) for item in data]
        except FileNotFoundError:
            print("No existing `students.json` file. Loading example.")
            return [
                    Student("Alice", "alice@example.com", "Mathematics", "11:00")
                    ]


    def add_student(
        self, name: str, contact_info: str, course: str, preferred_time: str
    ):
        """Add a student with a name, contact info, course, and preferred reminder time."""
        student = Student(name, contact_info, course, preferred_time)
        self.students.append(student)
        self.save_students()


    def remove_student(self, name) -> None:
        """Remove a student by name."""
        self.students = [s for s in self.students if s.name != name]
        self.save_students()

    
    def remove_student_by_id(self, student_id) -> Student:
        """Pops a student off the student list using the provided id and returns it."""
        return self.students.pop(student_id)


    def save_students(self) -> None:
        """Serialize and save the student list to file."""
        with open(self.file_path, "w") as file:
            json.dump(self.get_students_serialized(), file, indent=4)


    def get_students(self) -> List[Student]:
        """Retrieve list of students."""
        return self.students


    def get_students_serialized(self) -> List[Dict[str, Any]]:
        """Retrieve serialized list of students."""
        return [asdict(s) for s in self.students]


    def list_students(self) -> None:
        """Print all students to console."""
        for student in self.students:
            print(f"Name: {student.name}, Email: {student.contact_info}, Course: {student.course}, Preferred time: {student.preferred_time}")
