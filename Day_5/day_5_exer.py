from dataclasses import dataclass

@dataclass
class Student:
    name : str
    marks : int

    def grade(self):
        if self.marks >= 90:
            return "A"
        elif self.marks >= 80:
            return "B"
        elif self.marks >= 70:
            return "C"
        else:
            return "Fail"


class StudentService:
    def __init__(self):
         self.students : list[Student] = []
    

    def add_student(self, name : str, marks : int) -> None:

        """
        It adds the students in the student record
        """
        self.validate_records(name, marks)

        if any(student.name == name for student in self.students):
            raise ValueError(f"Student: {name} already in the database")
        
        self.students.append(Student(name, marks))
            

    def validate_records(self, name : str, marks : int):
            
            """
            It checks the name and marks valid to be added
            """
            if 0 > marks or marks > 100 :
                raise ValueError("Marks should between 0 and 100")
            if not name:
                raise ValueError("Name must be not Null")
            
            return True

    def get_grade(self, name : str) -> str:

        """
        It prints the grade of the required student
        """
        for s in self.students:
            if s.name == name:
                return s.grade()
        return None


service = StudentService()

service.add_student("Kishore", 98)
service.add_student("Velu", 80)
service.add_student("luffy", 90)

print(service.get_grade("Kishore"))