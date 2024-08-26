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
PART_TIME_HOUR = 4

def employee_attendance():
    '''
          Description: 
                this function is displaying employee present or not
          Parameters: 
                no peramters
          Return : 
                returns 1 for fulltime 2 for parttime and 0 for absent
    '''
    return random.randint(0,2)
    

def daily_employee_wage(status,hours_per_day):
    '''
          Description: 
                this function is calculating daily wage of employee
          Parameters: 
               hours_per_day : The number of hours the employee worked based on emp type i.e fulltime or parttime
          Return : 
                Returns the wage for an employee
    '''
    match status:
        case 1:
            return WAGE_PER_HOUR*hours_per_day
        case 2:
            return WAGE_PER_HOUR* hours_per_day
        case 0:
            return 0



def main():
    print("Welcome to EmployeeWage Computation Program on Master Branch")
    attendance = employee_attendance()
    if attendance == 1:
        print(f'Employee is FULLTIME Employee')
        print(f'Daily Employee Wage is : {daily_employee_wage(1,FULL_DAY_HOUR)}')
    elif attendance ==2:
        print(f'Employee is PARTTIME Employee')
        print(f'Daily Employee Wage is : {daily_employee_wage(2,PART_TIME_HOUR)}')
    else:
        print(f'Employee is Absent')
        print(f'Daily Employee Wage is : {0}')


if __name__=="__main__":
    main()