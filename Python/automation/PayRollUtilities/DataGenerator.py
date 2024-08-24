import datetime
import pandas as pd
import faker
import random
import re

class DataGenerator:
    def __init__(self,path='/Users/Harshitha/Desktop/Python_coding/'):
        self.path=path
        self.fake = faker.Faker()
        self.employees = []
        self.salaries = []
        self.payrolls = []
        self.timesheets = []
        self.attendances = []
        self.leave_requests = []
        self.benefits = []
        self.tax_rates = []
        self.deductions = []
        self.performance_reviews = []
        self.bonuses = []
        

    def generate_employees(self, num_employees=100):
        for i in range(1, num_employees + 1):
            self.employees.append([
                i,
                self.fake.first_name(),
                self.fake.last_name(),
                self.fake.date_of_birth(minimum_age=22, maximum_age=60),
                random.choice(['Male', 'Female']),
                self.fake.date_between(start_date='-10y', end_date='today'),
                random.randint(1, 5),
                random.choice(['Software Engineer', 'HR Manager', 'Sales Representative', 'Financial Analyst', 'Marketing Specialist']),
                self.fake.email(),
                self.fake.phone_number(),
                self.fake.address()
            ])
        df_employees = pd.DataFrame(self.employees, columns=[
            'employee_id', 'first_name', 'last_name', 'date_of_birth', 
            'gender', 'hire_date', 'department_id', 'position', 
            'email', 'phone', 'address'
        ])
        df_employees['phone'] = df_employees['phone'].apply(lambda x: re.sub(r'\D', '', x))
        df_employees.to_csv(self.path+'employees.csv', index=False, header=True)


    def generate_departments(self):
        departments = [
            (1, 'Engineering', 1),
            (2, 'Human Resources', 2),
            (3, 'Sales', 3),
            (4, 'Finance', 4),
            (5, 'Marketing', 5)
        ]
        df_departments = pd.DataFrame(departments, columns=[
            'department_id', 'department_name', 'manager_id'
        ])
        df_departments.to_csv(self.path+'departments.csv', index=False)


    def generate_positions(self):
        positions = [
            (1, 'Software Engineer', 1, 80000),
            (2, 'HR Manager', 2, 70000),
            (3, 'Sales Representative', 3, 60000),
            (4, 'Financial Analyst', 4, 75000),
            (5, 'Marketing Specialist', 5, 65000)
        ]
        df_positions = pd.DataFrame(positions, columns=[
            'position_id', 'position_name', 'department_id', 'base_salary'
        ])
        df_positions.to_csv(self.path+'positions.csv', index=False)


    def generate_salaries(self, num_employees=100, years=10):
        for i in range(1, num_employees + 1):
            for year in range(years):
                pay_date = self.fake.date_between(start_date=f'-{10-year}y', end_date=f'-{9-year}y')
                base_salary = random.randint(50000, 100000)
                bonus = random.randint(0, 10000)
                deductions = random.randint(1000, 5000)
                self.salaries.append([i, base_salary, bonus, deductions, pay_date])
        df_salaries = pd.DataFrame(self.salaries, columns=[
            'employee_id', 'base_salary', 'bonus', 'deductions', 'pay_date'
        ])
        df_salaries.to_csv(self.path+'salaries.csv', index=False)


    def generate_payrolls(self, num_employees=100, pay_periods=24):
        for i in range(1, num_employees + 1):
            for _ in range(pay_periods):
                pay_period_start = self.fake.date_between(start_date='-10y', end_date='-1d')
                pay_period_end = pay_period_start + datetime.timedelta(days=14)
                total_hours_worked = random.randint(60, 80)
                overtime_hours = random.randint(0, 20)
                gross_pay = random.randint(2000, 4000)
                net_pay = gross_pay - random.randint(100, 500)
                pay_date = pay_period_end + datetime.timedelta(days=1)
                self.payrolls.append([
                    i, pay_period_start, pay_period_end, total_hours_worked, 
                    overtime_hours, gross_pay, net_pay, pay_date
                ])
        df_payroll = pd.DataFrame(self.payrolls, columns=[
            'employee_id', 'pay_period_start', 'pay_period_end', 
            'total_hours_worked', 'overtime_hours', 'gross_pay', 
            'net_pay', 'pay_date'
        ])
        df_payroll.to_csv(self.path+'payroll.csv', index=False)


    def generate_timesheets(self, num_employees=100,years=10):
        for i in range(1, num_employees + 1):
            for _ in range(365 * years):
                # 10 years of daily records 
                date = self.fake.date_between(start_date='-10y', end_date='-1d')
                hours_worked = random.randint(0, 8)
                overtime_hours = random.randint(0, 2)
                self.timesheets.append([i, date, hours_worked, overtime_hours])
        df_timesheets = pd.DataFrame(self.timesheets, columns=[
            'employee_id', 'date', 'hours_worked', 'overtime_hours'])
        df_timesheets.to_csv(self.path+'timesheets.csv', index=False)

    def generate_attendances(self, num_employees=100,years=10):
        for i in range(1, num_employees + 1):
            for _ in range(365 * years):
                # 10 years of daily records
                date = self.fake.date_between(start_date='-10y', end_date='-1d')
                status = random.choice(['Present', 'Absent', 'Leave'])
                self.attendances.append([i, date, status])
        df_attendance = pd.DataFrame(self.attendances, columns=['employee_id', 'date', 'status'])
        df_attendance.to_csv(self.path+'attendance.csv', index=False)


    def generate_leave_requests(self, num_employees=100):
        for i in range(1, num_employees + 1):
            for _ in range(5):
                # Assume each employee makes about 5 leave requests over 10 years
                leave_type = random.choice(['Sick Leave', 'Vacation', 'Maternity/Paternity Leave'])
                start_date = self.fake.date_between(start_date='-10y', end_date='-1d')
                end_date = start_date + datetime.timedelta(days=random.randint(1, 15))
                reason = self.fake.sentence()
                status = random.choice(['Pending', 'Approved', 'Rejected'])
                self.leave_requests.append([i, leave_type, start_date, end_date, reason, status])
            df_leave_requests = pd.DataFrame(self.leave_requests, columns=['employee_id', 'leave_type', 'start_date', 'end_date', 'reason', 'status'])
            df_leave_requests.to_csv(self.path+'leave_requests.csv', index=False)

    def generate_benefits(self, num_employees=100,years=10):
        for i in range(1, num_employees + 1):
            for year in range(years):
                benefit_type = random.choice(['Health Insurance', 'Retirement Fund', 'Life Insurance'])
                benefit_amount = random.randint(1000, 5000)
                start_date = self.fake.date_between(start_date=f'-{10-year}y', end_date=f'-{9-year}y')
                end_date = start_date + datetime.timedelta(days=365)
                self.benefits.append([i, benefit_type, benefit_amount, start_date, end_date])
        df_benefits = pd.DataFrame(self.benefits, columns=['employee_id', 'benefit_type', 'benefit_amount', 'start_date', 'end_date'])
        df_benefits.to_csv(self.path+'benefits.csv', index=False)

    def generate_tax_rates(self, num_employees=100,years=10):
        for i in range(1, num_employees + 1):
            for year in range(years):
                effective_date = self.fake.date_between(start_date=f'-{10-year}y', end_date=f'-{9-year}y')
                tax_rate = round(random.uniform(15.0, 30.0), 2)
                self.tax_rates.append([i,effective_date, tax_rate])
        df_tax_rates = pd.DataFrame(self.tax_rates, columns=['tax_rate_id','effective_date', 'tax_rate'])
        df_tax_rates['effective_date'] = pd.to_datetime(df_tax_rates['effective_date'])
        df = df_tax_rates.drop_duplicates(subset='effective_date').copy()
        df.loc[:, 'year']  = df['effective_date'].dt.year
        df.loc[:, 'month']  = df['effective_date'].dt.month
        #  Group by Year and Month and filter to 2 rows per group
        filtered_df = df.groupby(['year', 'month']).head(2)
        sorted_df = filtered_df.sort_values(by='effective_date', ascending=False)
        sorted_df=sorted_df.drop(['year','month','tax_rate_id'],axis=1)
        sorted_df.to_csv(self.path+'tax_rates.csv',encoding='utf-8', index=False)


    def generate_deductions(self, num_employees=100,years=10):
        for i in range(1, num_employees + 1):
            for year in range(years):
                deduction_type = random.choice(['Health Insurance', 'Retirement Fund'])
                deduction_amount = random.randint(1000, 5000)
                effective_date = self.fake.date_between(start_date=f'-{10-year}y', end_date=f'-{9-year}y')
                self.deductions.append([i, deduction_type, deduction_amount, effective_date])
        df_deductions = pd.DataFrame(self.deductions, columns=['employee_id', 'deduction_type', 'deduction_amount', 'effective_date'])
        df_deductions.to_csv(self.path+'deductions.csv', index=False)


    def generate_performance_reviews(self, num_employees=100,years=10):
        for i in range(1, num_employees + 1):
            for year in range(years):
                review_date = self.fake.date_between(start_date=f'-{10-year}y', end_date=f'-{9-year}y')
                performance_score = round(random.uniform(1.0, 5.0), 2)
                comments = self.fake.sentence()
                self.performance_reviews.append([i, review_date, performance_score, comments])
        df_performance_reviews = pd.DataFrame(self.performance_reviews, columns=['employee_id', 'review_date', 'performance_score', 'comments'])
        df_performance_reviews.to_csv(self.path+'performance_reviews.csv', index=False)


    def generate_bonuses(self, num_employees=100,years=10):
        for i in range(1, num_employees + 1):
            for year in range(years):
                bonus_amount = random.randint(1000, 10000)
                reason = random.choice(['Year-end bonus', 'Performance bonus'])
                bonus_date = self.fake.date_between(start_date=f'-{10-year}y', end_date=f'-{9-year}y')
                self.bonuses.append([i, bonus_amount, reason, bonus_date])
        df_bonuses = pd.DataFrame(self.bonuses, columns=['employee_id', 'bonus_amount', 'reason', 'bonus_date'])
        df_bonuses.to_csv(self.path+'bonuses.csv', index=False)

    def generate_all(self):
        self.generate_employees()
        # Generate Departments
        self.generate_departments()
        # Generate Positions
        self.generate_positions()
        # Generate Salaries
        self.generate_salaries()
        # Generate Payrolls
        self.generate_payrolls()
        # Generate Timesheets
        self.generate_timesheets()
        # Generate Attendance
        self.generate_attendances()
        # Generate leave_requests
        self.generate_leave_requests()
        # Generate benefits
        self.generate_benefits()
        # Generate TaxRates
        self.generate_tax_rates()
        # Generate deductions
        self.generate_deductions()
        # Generate performance_reviews
        self.generate_performance_reviews()
        # Generate bonuses
        self.generate_bonuses()
        print("CSV's generated successfully")