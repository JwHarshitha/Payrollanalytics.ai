
import datetime
import pandas as pd
import faker
import random
import re

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------To create csv of Employees-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
fake = faker.Faker()
employees = []
for i in range(1, 101):
    employees.append([i, fake.first_name(), fake.last_name(), fake.date_of_birth(minimum_age=22, maximum_age=60), random.choice(['Male', 'Female']), fake.date_between(start_date='-10y', end_date='today'), random.randint(1, 5), random.choice(['Software Engineer', 'HR Manager', 'Sales Representative', 'Financial Analyst', 'Marketing Specialist']), fake.email(), fake.phone_number(), fake.address()])
    df_employees = pd.DataFrame(employees, columns=['employee_id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'hire_date', 'department_id', 'position', 'email', 'phone', 'address'])
    df_employees.to_csv('employees.csv', index=False)
#Clean the Phone Numbers Column from employees CSV-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def clean_phone_num(phone_num):
    return re.sub(r'\D', '', phone_num)

df=pd.read_csv(r"/Users/Harshitha/Desktop/Python_coding/employees.csv", encoding='utf-8')
df['phone'] = df['phone'].apply(clean_phone_num)
df.to_csv('/Users/Harshitha/Desktop/Python_coding/employee_new.csv', index=False,header=True)
print(df['phone'][1])

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ---------------------------------------To create csv of Departments----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
departments = [ (1, 'Engineering', 1), (2, 'Human Resources', 2), (3, 'Sales', 3), (4, 'Finance', 4), (5, 'Marketing', 5) ]
df_departments = pd.DataFrame(departments, columns=['department_id', 'department_name', 'manager_id'])
df_departments.to_csv('departments.csv', index=False)

# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# ----------------------------------------To create csv of Positions---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
positions = [ (1, 'Software Engineer', 1, 80000), (2, 'HR Manager', 2, 70000), (3, 'Sales Representative', 3, 60000), (4, 'Financial Analyst', 4, 75000), (5, 'Marketing Specialist', 5, 65000) ]
df_positions = pd.DataFrame(positions, columns=['position_id', 'position_name', 'department_id', 'base_salary'])
df_positions.to_csv('positions.csv', index=False)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------To create csv of Salaries--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fake = faker.Faker()
salaries = []
for i in range(1, 101):
    for year in range(10):
        pay_date = fake.date_between(start_date=f'-{10-year}y', end_date=f'-{9-year}y')
        base_salary = random.randint(50000, 100000)
        bonus = random.randint(0, 10000)
        deductions = random.randint(1000, 5000)
        salaries.append([i, base_salary, bonus, deductions, pay_date])
        df_salaries = pd.DataFrame(salaries, columns=['employee_id', 'base_salary', 'bonus', 'deductions', 'pay_date'])
        df_salaries.to_csv('salaries.csv', index=False)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------To create csv of Payrolls--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fake = faker.Faker()
payrolls = []
for i in range(1, 101):
    for _ in range(24):
        pay_period_start = fake.date_between(start_date='-10y', end_date='-1d')
        pay_period_end = pay_period_start + datetime.timedelta(days=14)
        total_hours_worked = random.randint(60, 80)
        overtime_hours = random.randint(0, 20)
        gross_pay = random.randint(2000, 4000)
        net_pay = gross_pay - random.randint(100, 500)
        pay_date = pay_period_end + datetime.timedelta(days=1)
        payrolls.append([i, pay_period_start, pay_period_end, total_hours_worked, overtime_hours, gross_pay, net_pay, pay_date])
        df_payroll = pd.DataFrame(payrolls, columns=['employee_id', 'pay_period_start', 'pay_period_end', 'total_hours_worked', 'overtime_hours', 'gross_pay', 'net_pay', 'pay_date'])
df_payroll.to_csv('payroll.csv', index=False)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------To create csv of Timesheets--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fake = faker.Faker()
timesheets = []
for i in range(1, 101):
    for _ in range(365 * 10):
        # 10 years of daily records 
        date = fake.date_between(start_date='-10y', end_date='-1d')
        hours_worked = random.randint(0, 8)
        overtime_hours = random.randint(0, 2)
        timesheets.append([i, date, hours_worked, overtime_hours])
        df_timesheets = pd.DataFrame(timesheets, columns=['employee_id', 'date', 'hours_worked', 'overtime_hours'])
        df_timesheets.to_csv('timesheets.csv', index=False)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------To create csv of Attendances--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fake = faker.Faker()
attendances = []
for i in range(1, 101):
    for _ in range(365 * 10):
        # 10 years of daily records
        date = fake.date_between(start_date='-10y', end_date='-1d')
        status = random.choice(['Present', 'Absent', 'Leave'])
        attendances.append([i, date, status])
        df_attendance = pd.DataFrame(attendances, columns=['employee_id', 'date', 'status'])
        df_attendance.to_csv('attendance.csv', index=False)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------To create csv of Leave Requests--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fake = faker.Faker()
leave_requests = []
for i in range(1, 101):
    for _ in range(5):
        # Assume each employee makes about 5 leave requests over 10 years
        leave_type = random.choice(['Sick Leave', 'Vacation', 'Maternity/Paternity Leave'])
        start_date = fake.date_between(start_date='-10y', end_date='-1d')
        end_date = start_date + datetime.timedelta(days=random.randint(1, 15))
        reason = fake.sentence()
        status = random.choice(['Pending', 'Approved', 'Rejected'])
        leave_requests.append([i, leave_type, start_date, end_date, reason, status])
        df_leave_requests = pd.DataFrame(leave_requests, columns=['employee_id', 'leave_type', 'start_date', 'end_date', 'reason', 'status'])
        df_leave_requests.to_csv('leave_requests.csv', index=False)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------To create csv of Benefits--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fake = faker.Faker()
benefits = []
for i in range(1, 101):
    for year in range(10):
        benefit_type = random.choice(['Health Insurance', 'Retirement Fund', 'Life Insurance'])
        benefit_amount = random.randint(1000, 5000)
        start_date = fake.date_between(start_date=f'-{10-year}y', end_date=f'-{9-year}y')
        end_date = start_date + datetime.timedelta(days=365)
        benefits.append([i, benefit_type, benefit_amount, start_date, end_date])
        df_benefits = pd.DataFrame(benefits, columns=['employee_id', 'benefit_type', 'benefit_amount', 'start_date', 'end_date'])
        df_benefits.to_csv('benefits.csv', index=False)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------To create csv of Tax_rates--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fake = faker.Faker()
tax_rates = []
for i in range(1, 101):
    for year in range(10):
        effective_date = fake.date_between(start_date=f'-{10-year}y', end_date=f'-{9-year}y')
        tax_rate = round(random.uniform(15.0, 30.0), 2)
        tax_rates.append([i,effective_date, tax_rate])
        df_tax_rates = pd.DataFrame(tax_rates, columns=['tax_rate_id','effective_date', 'tax_rate'])
        df_tax_rates.to_csv('/Users/Harshitha/Desktop/Python_coding/tax_rates.csv', index=False)

# Drop duplicates& sort the values of tax rates------------

df_s=pd.read_csv("/Users/Harshitha/Desktop/Python_coding/tax_rates.csv")
df_s['effective_date'] = pd.to_datetime(df_s['effective_date'])
df = df_s.drop_duplicates(subset='effective_date').copy()
df.loc[:, 'year']  = df['effective_date'].dt.year
df.loc[:, 'month']  = df['effective_date'].dt.month

#  Group by Year and Month and filter to 2 rows per group
filtered_df = df.groupby(['year', 'month']).head(2)
sorted_df = filtered_df.sort_values(by='effective_date', ascending=False)
sorted_df=sorted_df.drop(['year','month','tax_rate_id'],axis=1)

sorted_df.to_csv('/Users/Harshitha/Desktop/Python_coding/tax_rates_sorted.csv',encoding='utf-8', index=False)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------To create csv of Deductions--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fake = faker.Faker()
deductions = []
for i in range(1, 101):
    for year in range(10):
        deduction_type = random.choice(['Health Insurance', 'Retirement Fund'])
        deduction_amount = random.randint(1000, 5000)
        effective_date = fake.date_between(start_date=f'-{10-year}y', end_date=f'-{9-year}y')
        deductions.append([i, deduction_type, deduction_amount, effective_date])
        df_deductions = pd.DataFrame(deductions, columns=['employee_id', 'deduction_type', 'deduction_amount', 'effective_date'])
        df_deductions.to_csv('deductions.csv', index=False)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------To create csv of Performance Reviews--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fake = faker.Faker()
performance_reviews = []
for i in range(1, 101):
    for year in range(10):
        review_date = fake.date_between(start_date=f'-{10-year}y', end_date=f'-{9-year}y')
        performance_score = round(random.uniform(1.0, 5.0), 2)
        comments = fake.sentence()
        performance_reviews.append([i, review_date, performance_score, comments])
        df_performance_reviews = pd.DataFrame(performance_reviews, columns=['employee_id', 'review_date', 'performance_score', 'comments'])
        df_performance_reviews.to_csv('performance_reviews.csv', index=False)
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# -----------------------------------------To create csv of Bonuses--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# fake = faker.Faker()
bonuses = []
for i in range(1, 101):
    for year in range(10):
        bonus_amount = random.randint(1000, 10000)
        reason = random.choice(['Year-end bonus', 'Performance bonus'])
        bonus_date = fake.date_between(start_date=f'-{10-year}y', end_date=f'-{9-year}y')
        bonuses.append([i, bonus_amount, reason, bonus_date])
        df_bonuses = pd.DataFrame(bonuses, columns=['employee_id', 'bonus_amount', 'reason', 'bonus_date'])
        df_bonuses.to_csv('bonuses.csv', index=False)