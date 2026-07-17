class AgeNotSufficient(Exception):
    pass



def age_calculator(age : int):
    if(age >= 18):
        raise AgeNotSufficient("Age must greater than 18 to get voter id")

result = age_calculator(18)
        
