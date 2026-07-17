class Student:

    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):

        if value < 18:
            print("Too Young")
            return

        self._age = value


student = Student(20)
print(student.age)
student.age = 15
print(student.age)