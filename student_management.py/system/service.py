from student import Student
from validate import is_name_valid, is_rollno_valid, is_department_valid, is_graduation_year_valid, marks_are_valid

import logging
logging.basicConfig(filename= 'records.log', level= logging.INFO)
logger = logging.getLogger(__name__)

class StudentService:

    def __init__(self):
        self.Students : list[Student]

    def add_students(self, name : str, rollno : int, marks : list, dept : str, year : int):

        """
        It adds the Student to the database if all the inputs are valid
        """
        if is_name_valid(name) or is_rollno_valid(rollno) or is_department_valid(dept) or is_graduation_year_valid(year) or marks_are_valid(marks):
            logger.error("Check the Given credentials properly...")
            return
        if any(student.rollno == rollno for student in self.Students):
            logger.error("Student with this roll number already registered")
        
        self.Students.append(Student(name,rollno,marks,dept,year))

    def get_average_mark(self, name : str):

        """
        It returns the Average mark of the Student
        """
        for student in self.Students:
            if name == student.name:
                average = sum(student.marks) / len(student.marks)
                return average
        raise ValueError("Student name not found")
        
            