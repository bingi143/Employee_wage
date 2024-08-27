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
TOTAL_WORK_DAYS_PER_MONTH=20
TOTAL_WORK_HOURS_PER_MONTH=100
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


def employee_monthly_wage():
    '''
          Description: 
                this function is calculating monthly wage of employee
          Parameters: 
               None
          Return : 
                Returns the monthly wage for an employee
    '''
    monthly_wage=0
    wage_list_each_day=[]
    hours=0
    days=0
    while hours<TOTAL_WORK_HOURS_PER_MONTH and days<TOTAL_WORK_DAYS_PER_MONTH:
        for day in range(TOTAL_WORK_DAYS_PER_MONTH):
            attendance=employee_attendance()
            if attendance == 1:
                monthly_wage+=daily_employee_wage(1,FULL_DAY_HOUR)
                wage_list_each_day.append(daily_employee_wage(1,FULL_DAY_HOUR))
                hours+=FULL_DAY_HOUR
                days+=1

            elif attendance ==2:
                monthly_wage+=daily_employee_wage(2,PART_TIME_HOUR)
                wage_list_each_day.append(daily_employee_wage(2,PART_TIME_HOUR))
                hours+=PART_TIME_HOUR
                days+=1

            else:
                wage_list_each_day.append(0)
                days+=1

    return monthly_wage,wage_list_each_day


def main():
    print("Welcome to EmployeeWage Computation Program on Master Branch")
    total_wage,list_each_days_wage=employee_monthly_wage()
    print("total monthly wage of employee is:",total_wage)
    print("list of each days earning",list_each_days_wage)
    

if __name__=="__main__":
    main()