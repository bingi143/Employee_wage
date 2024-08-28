'''

@Author: Venkatesh
@Date: 2024-08-26 18:00:30
@Last Modified by: Author Name
@Last Modified time: 2024-08-26 18:00:30
@Title : Program Aim
Python Program DocString Structure:

''' 


import random

class EmployeeWage:

    
    FULL_DAY_HOUR = 8
    PART_TIME_HOUR = 4

    @classmethod
    def employee_attendance(cls):
        '''
                Description: 
                    this function is displaying employee present or not
                Parameters: 
                    no peramters
                Return : 
                    returns 1 for fulltime 2 for parttime and 0 for absent
        '''
        return random.randint(0,2)

    @classmethod
    def daily_employee_wage(cls,status,hours_per_day,wage_per_hour):
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
                return wage_per_hour*hours_per_day
            case 2:
                return wage_per_hour* hours_per_day
            case 0:
                return 0

    @classmethod
    def employee_monthly_wage(cls,company):
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
        while hours<company.total_work_hours_in_month and days<company.total_work_days_in_month:
            for day in range(company.total_work_days_in_month):
                attendance=EmployeeWage.employee_attendance()
                if attendance == 1:
                    monthly_wage+=EmployeeWage.daily_employee_wage(1,cls.FULL_DAY_HOUR,company.wage_per_hour)
                    wage_list_each_day.append(EmployeeWage.daily_employee_wage(1,cls.FULL_DAY_HOUR,company.wage_per_hour))
                    hours+=cls.FULL_DAY_HOUR
                    days+=1

                elif attendance ==2:
                    monthly_wage+=EmployeeWage.daily_employee_wage(2,cls.PART_TIME_HOUR,company.wage_per_hour)
                    wage_list_each_day.append(EmployeeWage.daily_employee_wage(2,cls.PART_TIME_HOUR,company.wage_per_hour))
                    hours+=cls.PART_TIME_HOUR
                    days+=1

                else:
                    wage_list_each_day.append(0)
                    days+=1

        return monthly_wage,days,hours,wage_list_each_day
    
    
class Company:

    def __init__(self,company_name,wage_per_hour,total_work_days_in_month,total_work_hour_in_month):
         self.company_name=company_name
         self.wage_per_hour=wage_per_hour
         self.total_work_days_in_month=total_work_days_in_month
         self.total_work_hours_in_month=total_work_hour_in_month


class EmpWageBuilder:

    def __init__(self):
        self.companies = []

    def add_company(self, company):
        self.companies.append(company)

    def display_companies(self):
        print("List of company names:")
        for company in self.companies:
            print(f"******************\n{company.company_name}")

    def display_wages(self):
        for company in self.companies:
            employee_wage = EmployeeWage(company)
            monthly_wage, working_days, working_hours, day_wise_wage = employee_wage.employee_monthly_wage()
            
            print("-" * 30)
            print(f"Company Name: {company.company_name}")
            print(f"Monthly Wage: {monthly_wage}")
            print(f"Total Working Days: {working_days}")
            print(f"Total Working Hours: {working_hours}")
            print(f"Daily Wage: {day_wise_wage}")
            print("-" * 30)


def main():
    print("Welcome to EmployeeWage Computation ")
    companies=[]
    while True:
        try:
            option = int(input('''Enter           
                    1: to add company 
                    2: to display all companies
                    3: to diplay wages for all companies
                    4: to exit: '''))
            
            if option == 1:
                company_name = input("Enter the company name: ")
                total_work_days_in_month = int(input("Enter the total working days per month: "))
                total_work_hours_in_month = int(input("Enter the maximum working hours per month: "))
                wage_per_hour = int(input("Enter the wage per hour: "))
                company1=Company(company_name,wage_per_hour,total_work_days_in_month,total_work_hours_in_month)
                companies.append(company1)
                print(f"***company {company_name} added succussfully")

            elif option == 2:
                print("List of company names:")
                for company in companies:
                    print("******************")
                    print(f"{company.company_name}")

            elif option==3:
                for company in companies:
                    monthly_wage, working_days, working_hours,day_wise_wage = EmployeeWage.employee_monthly_wage(company)
            
                    print("-"*30+"\n"+f"Company Name: {company.company_name}")
                    print(f"Monthly Wage: {monthly_wage}")
                    print(f"Total Working Days: {working_days}")
                    print(f"Total Working Hours: {working_hours}")
                    print(f"Daily wage: {day_wise_wage}"+"\n"+"-"*30)

            elif option == 4:
               break

            else:
               print("Invalid option. Please enter a number between 1 and 4.")
               
        except ValueError:
            print("Please enter correct number")


if __name__=="__main__":
    main()