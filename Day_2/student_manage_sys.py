import logging
logger = logging.getLogger(__name__)

def mark_isvalid(mark : int) -> bool:
    """
    Check if the marks are valid
    """
    if(mark >= 0 and mark <= 100):
        return True
    return False

def calculate_average(marks : list) -> int:
    """
    It calculates the Average of the Student
    """
    return sum(marks) / len(marks)

def calculate_grade(avg : int) -> str:
    """
    It calculates the Grade of the Student by the average
    """
    if(35 > avg <= 50):
        return 'C'
    elif(50 < avg <= 75):
        return 'B'
    else:
        return 'A'

def write_records_on_file(name : str, avg : int, grade : str) -> None:
    """
    It stores the records on the file
    """
    try:
        with open("students_records.txt", "a") as file:
            file.write("Student Name" + name | "Average_marks" + avg | "Grade" + grade)
            print("Record Updated !!")
    except OSError as e:
        logger.error("Failed to fetch")

name = str(input())
marks=[]
subjects = int(input())
for i in range(0,subjects):
    mark = int(input())
    if(mark_isvalid(mark)):
        marks.append(mark)
avg = calculate_average(marks)
grade = calculate_grade(avg)

print(f"Name : {name} | Marks : {marks} | Average : {avg} | Grade : {grade}")

    
