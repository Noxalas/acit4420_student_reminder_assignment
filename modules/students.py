from dataclasses import dataclass, asdict
from typing import List, Dict, Any

@dataclass
class Student:
    name: str 
    contact_info: str 
    course: str
    preferred_time: str 


class Students:
    def __init__(self):
        self.students: List[Student] = []


    def add_student(
        self, name: str, contact_info: str, course: str, preferred_time: str
    ):
        """Add a student with a name, contact info, course, and preferred reminder time"""
        student = Student(name, contact_info, course, preferred_time)

        self.students.append(student)


    def remove_student(self, name) -> None:
        """Remove a student by name."""
        self.students = [s for s in self.students if s.name != name]


    def get_students(self) -> List[Student]:
        """Retrieve list of students"""
        return self.students


    def get_students_serialized(self) -> List[Dict[str, Any]]:
        """Retrieve serialized list of students"""
        return [asdict(s) for s in self.students]
