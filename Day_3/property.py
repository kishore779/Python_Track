class Temperature:
    def __init__(self, celsius):
        self._celsius = celsius

    @property
    def celsius(self):
        print("Fetching result...")
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below zero")
        print("Setting value")
        self._celsius = value

    @property
    def fahernheit(self):
        return (self._celsius * 9 / 5) + 32


temp = Temperature(30)
print(temp.celsius)
temp.celsius = 30
print(temp.fahernheit)
temp.celsius = 300


# class Student:

#     def __init__(self, age):
#         self._age = age

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, value):

#         if value < 18:
#             print("Too Young")
#             return

#         self._age = value


# student = Student(20)
# print(student.age)
# student.age = 15
# print(student.age)
