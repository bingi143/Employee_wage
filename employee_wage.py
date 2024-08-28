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
            This function checks whether the employee is present or not.
        Parameters: 
            No parameters.
        Return: 
            Returns 1 for full-time, 2 for part-time, and 0 for absent.
        '''
        return random.randint(0, 2)

    @classmethod
    def daily_employee_wage(cls, status, wage_per_hour):
        '''
        Description: 
            This function calculates the daily wage of an employee.
        Parameters: 
            status : The attendance status of the employee (1 for full-time, 2 for part-time, 0 for absent).
            wage_per_hour: The wage per hour for the employee.
        Return: 
            Returns the wage for the employee.
        '''
        hours_per_day = cls.FULL_DAY_HOUR if status == 1 else cls.PART_TIME_HOUR
        return wage_per_hour * hours_per_day

    @classmethod
    def employee_monthly_wage(cls, company_emp_wage):
        '''
        Description: 
            This function calculates the monthly wage of an employee.
        Parameters: 
            company_emp_wage: The CompanyEmpWage object containing company and employee information.
        Return: 
            Updates the monthly wage, total days worked, total hours worked, and a list of daily wages in the CompanyEmpWage object.
        '''
        company_emp_wage.monthly_wage = 0
        company_emp_wage.wage_list_each_day = []
        hours = 0
        days = 0

        while hours < company_emp_wage.company.total_work_hours_in_month and days < company_emp_wage.company.total_work_days_in_month:
            attendance = cls.employee_attendance()
            if attendance == 1 or attendance == 2:
                daily_wage = cls.daily_employee_wage(attendance, company_emp_wage.company.wage_per_hour)
                company_emp_wage.monthly_wage += daily_wage
                company_emp_wage.wage_list_each_day.append(daily_wage)
                hours += cls.FULL_DAY_HOUR if attendance == 1 else cls.PART_TIME_HOUR
            else:
                company_emp_wage.wage_list_each_day.append(0)
            days += 1

        company_emp_wage.total_working_days = days
        company_emp_wage.total_working_hours = hours


class Company:
    def __init__(self, company_name, wage_per_hour, total_work_days_in_month, total_work_hours_in_month):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.total_work_days_in_month = total_work_days_in_month
        self.total_work_hours_in_month = total_work_hours_in_month
        self.employees = []

    def add_employee(self, employee_name):
        '''
        Description: 
            Adds an employee to the company.
        Parameters: 
            employee_name: The name of the employee.
        Return:
            None
        '''
        employee_id = len(self.employees) + 1
        self.employees.append({'id': employee_id, 'name': employee_name})

    def update_employee(self, employee_id, new_name):
        '''
        Description: 
            Updates the name of an employee.
        Parameters: 
            employee_id: The ID of the employee to update.
            new_name: The new name of the employee.
        Return:
            None
        '''
        for emp in self.employees:
            if emp['id'] == employee_id:
                emp['name'] = new_name
                print(f"*** Employee ID {employee_id} name updated to {new_name} ***")
                return
        print(f"Employee with ID {employee_id} not found.")

    def delete_employee(self, employee_id):
        '''
        Description: 
            Deletes an employee from the company.
        Parameters: 
            employee_id: The ID of the employee to delete.
        Return:
            None
        '''
        for emp in self.employees:
            if emp['id'] == employee_id:
                self.employees.remove(emp)
                print(f"*** Employee ID {employee_id} deleted ***")
                return
        print(f"Employee with ID {employee_id} not found.")

    def update_company(self, new_name=None, new_wage_per_hour=None, new_total_work_days=None, new_total_work_hours=None):
        '''
        Description: 
            Updates the company details.
        Parameters: 
            new_name: The new name of the company.
            new_wage_per_hour: The new wage per hour.
            new_total_work_days: The new total work days in a month.
            new_total_work_hours: The new total work hours in a month.
        Return:
            None
        '''
        if new_name:
            self.company_name = new_name
        if new_wage_per_hour:
            self.wage_per_hour = new_wage_per_hour
        if new_total_work_days:
            self.total_work_days_in_month = new_total_work_days
        if new_total_work_hours:
            self.total_work_hours_in_month = new_total_work_hours
        print(f"*** Company details updated successfully ***")


class CompanyEmpWage:
    def __init__(self, company, employee):
        self.company = company
        self.employee = employee
        self.monthly_wage = 0
        self.wage_list_each_day = []
        self.total_working_days = 0
        self.total_working_hours = 0


class EmpWageBuilder:
    def __init__(self):
        self.company_emp_wages = []

    def add_company_emp_wage(self, company_emp_wage):
        '''
        Description: 
            Adds a CompanyEmpWage object to the list.
        Parameters: 
            company_emp_wage: The CompanyEmpWage object.
        '''
        self.company_emp_wages.append(company_emp_wage)

    def delete_company(self, company_name):
        '''
        Description: 
            Deletes a company and all associated employee wages.
        Parameters: 
            company_name: The name of the company to delete.
        Return:
            None
        '''
        for company_emp_wage in self.company_emp_wages:
            if company_emp_wage.company.company_name == company_name:
                self.company_emp_wages.remove(company_emp_wage)
        print(f"*** Company {company_name} and all associated employee data deleted ***")

    def display_companies_and_employees(self):
        '''
        Description: 
            Displays all companies and their employees.
        '''
        for company_emp_wage in self.company_emp_wages:
            company = company_emp_wage.company
            print(f"Company: {company.company_name}")
            for emp in company.employees:
                print(f"Employee ID: {emp['id']}, Name: {emp['name']}")
            print("-" * 30)

    def display_wages(self):
        '''
        Description: 
            Displays the wages of all employees in all companies.
        Parameters:
            self
        Return:
            None
        '''
        for company_emp_wage in self.company_emp_wages:
            EmployeeWage.employee_monthly_wage(company_emp_wage)
            print("-" * 30)
            print(f"Company Name: {company_emp_wage.company.company_name}")
            print(f"Employee Name: {company_emp_wage.employee['name']}")
            print(f"Monthly Wage: {company_emp_wage.monthly_wage}")
            print(f"Total Working Days: {company_emp_wage.total_working_days}")
            print(f"Total Working Hours: {company_emp_wage.total_working_hours}")
            print(f"Daily Wage: {company_emp_wage.wage_list_each_day}")
            print("-" * 30)


def main():
    print("Welcome to Employee Wage Computation")
    emp_wage_builder = EmpWageBuilder()
    
    companies = []
    
    while True:
        try:
            option = int(input('''Enter           
                1: to add company 
                2: to add employee to company
                3: to update employee in company
                4: to delete employee from company
                5: to update company details
                6: to delete a company
                7: to display all companies and their employees
                8: to display wages for all companies
                9: to exit: '''))
            
            if option == 1:
                company_name = input("Enter the company name: ")
                total_work_days_in_month = int(input("Enter the total working days per month: "))
                total_work_hours_in_month = int(input("Enter the maximum working hours per month: "))
                wage_per_hour = int(input("Enter the wage per hour: "))
                company = Company(company_name, wage_per_hour, total_work_days_in_month, total_work_hours_in_month)
                companies.append(company)
                print(f"*** Company {company_name} added successfully ***")

            elif option == 2:
                company_name = input("Enter the company name to add an employee: ")
                employee_name = input("Enter the employee name: ")
                for company in companies:
                    if company.company_name == company_name:
                        company.add_employee(employee_name)
                        company_emp_wage = CompanyEmpWage(company, company.employees[-1])
                        emp_wage_builder.add_company_emp_wage(company_emp_wage)
                        print(f"*** Employee {employee_name} added to company {company_name} ***")
                        break
                else:
                    print(f"Company {company_name} not found.")

            elif option == 3:
                company_name = input("Enter the company name: ")
                employee_id = int(input("Enter the employee ID to update: "))
                new_name = input("Enter the new employee name: ")
                for company in companies:
                    if company.company_name == company_name:
                        company.update_employee(employee_id, new_name)
                        break
                else:
                    print(f"Company {company_name} not found.")

            elif option == 4:
                company_name = input("Enter the company name: ")
                employee_id = int(input("Enter the employee ID to delete: "))
                for company in companies:
                    if company.company_name == company_name:
                        company.delete_employee(employee_id)
                        break
                else:
                    print(f"Company {company_name} not found.")

            elif option == 5:
                company_name = input("Enter the company name to update: ")
                for company in companies:
                    if company.company_name == company_name:
                        new_name = input("Enter new company name (press Enter to skip): ")
                        new_wage_per_hour = input("Enter new wage per hour (press Enter to skip): ")
                        new_total_work_days = input("Enter new total work days per month (press Enter to skip): ")
                        new_total_work_hours = input("Enter new total work hours per month (press Enter to skip): ")
                        
                        # Convert to appropriate types if provided
                        new_wage_per_hour = int(new_wage_per_hour) if new_wage_per_hour else None
                        new_total_work_days = int(new_total_work_days) if new_total_work_days else None
                        new_total_work_hours = int(new_total_work_hours) if new_total_work_hours else None
                        
                        company.update_company(new_name, new_wage_per_hour, new_total_work_days, new_total_work_hours)
                        break
                else:
                    print(f"Company {company_name} not found.")

            elif option == 6:
                company_name = input("Enter the company name to delete: ")
                emp_wage_builder.delete_company(company_name)
                companies = [company for company in companies if company.company_name != company_name]

            elif option == 7:
                emp_wage_builder.display_companies_and_employees()

            elif option == 8:
                emp_wage_builder.display_wages()

            elif option == 9:
                break

            else:
                print("Invalid option. Please enter a number between 1 and 9.")
               
        except ValueError:
            print("Please enter a correct number")


if __name__ == "__main__":
    main()
