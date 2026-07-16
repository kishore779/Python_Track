class Student:
    collage = "KPR"
    total_students = 100

    @classmethod
    def show_total_students(cls):
        print(cls.total_students)

    def __init__(self, name : str, dept : str, cgpa : int):
        self.name = name
        self.dept = dept
        self.cgpa = cgpa

    def display(self):
        """
        Intance method
        """
        print(f"Name : {self.name} | Dept : {self.dept} | CGPA : {self.cgpa} | College : {self.collage}")
    
    @staticmethod
    def valid_age(age : int):
        """
        Static method
        """
        if age > 18:
            return True

student1 = Student("kishore","cse",9.7)
student1.display()
Student.show_total_students()
    
        