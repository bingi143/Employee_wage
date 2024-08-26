'''

@Author: Venkatesh
@Date: 2024-08-26 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2024-08-26 18:00:30
@Title : Program Aim
Python Program DocString Structure:

''' 


import random

WAGE_PER_HOUR = 20
FULL_DAY_HOUR = 8

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
    

def daily_employee_wage():
    '''
          Description: 
                this function is calculating daily wage of employee
          Parameters: 
                per_hour(int): how much amount per hour
                daily_hours(int): how many hours working in a day
          Return : 
                None
    '''
    return WAGE_PER_HOUR*FULL_DAY_HOUR


def main():
    print("Welcome to EmployeeWage Computation Program on Master Branch")
    attendance = employee_attendance()
    if attendance == 'present':
        print(f'Daily Employee Wage is : {daily_employee_wage()}')
    else:
        print(f'Daily Employee Wage is : {0}')


if __name__=="__main__":
    main()