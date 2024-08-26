'''

@Author: Venkatesh
@Date: 2024-08-26 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2024-08-26 18:00:30
@Title : Program Aim
Python Program DocString Structure:

''' 


import random

def employee_attendance():
    '''
          Description: 
                this function is displaying employee present or not
          Parameters: 
                no peramters
          Return : 
                "present" (str): if employee is present
                "absent" (str): if employee is absent
    '''
    attendance=random.randint(0,1)
    if attendance==0:
        return "present"
    else:
        return "absent"

def main():
    print("Welcome to EmployeeWage Computation Program")
    print("employee is:",employee_attendance())


if __name__=="__main__":
    main()

