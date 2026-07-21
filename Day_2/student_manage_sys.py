import logging

logger = logging.getLogger(__name__)


def mark_isvalid(mark: int) -> bool:
    """
    Check if the marks are valid
    """
    return 0 <= mark <= 100


def calculate_average(marks: list) -> int:
    """
    It calculates the Average of the Student
    """
    return sum(marks) / len(marks)


def calculate_grade(avg: int) -> str:
    """
    It calculates the Grade of the Student by the average
    """
    if avg > 75:
        return "A"
    elif 50 < avg <= 75:
        return "B"
    elif 35 <= avg:
        return "C"
    else:
        return "F"


def write_records_on_file(name: str, marks: list[int], avg: int, grade: str) -> None:
    """
    It stores the records on the file
    """
    try:
        with open(f"{name}_records.txt", "w") as file:
            file.write(
                "Student Name {name} | Average_marks + {avg:.2f} | Grade + {grade}\n"
            )
            for i, marks in enumerate(marks):
                file.write(f"Subject {i} : {mark}\n")
            print("Record Updated !!")
    except OSError as e:
        logger.error(f"Failed to fetch : {e}")


name = str(input())
marks = []
subjects = int(input())
for i in range(0, subjects):
    mark = int(input())
    if mark_isvalid(mark):
        marks.append(mark)
avg = calculate_average(marks)
grade = calculate_grade(avg)

write_records_on_file(name, marks, avg, grade)
print(f"Name : {name} | Marks : {marks} | Average : {avg} | Grade : {grade}")
