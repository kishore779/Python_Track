from dataclasses import dataclass

@dataclass
class Student:
    name : str
    rollno : int
    marks : list
    dept : str
    year : int