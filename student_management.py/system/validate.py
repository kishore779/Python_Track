class ValidationError(Exception):
    pass

def is_name_valid(name : str):

    """
    It check if the Student name is valid
    """
    if not name or not name.strip():
        raise ValidationError("Name is needed to store student record")

def is_rollno_valid(rollno : int):

    """
    It check if the Student rollno is valid
    """
    if not 0 < rollno <= 100:
        raise ValidationError("Roll no must be in btw 1 and 100")

def marks_are_valid(marks : list):

    """
    It check if the Student marks are valid
    """

    for mark in marks:
        if not mark < 0 or mark > 100:
            raise ValidationError("Marks should be in 0 and 100") 
    return True

def is_department_valid(dept : str):

    """
    Checks the Department are present in college
    """
    departments = ["CSE", "IT", "ECE", "MECH", "CIVIL"]

    if not dept in departments:
        raise ValidationError("Choose the available departments")

def is_graduation_year_valid(grad_year :int) -> bool:

    """
    Checks it is a valid Graduation year
    """
    years = [2027, 2028, 2029, 2030]

    if grad_year in years:
        raise ValidationError("Choose the valid graduation year")