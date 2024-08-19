
'''''class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return self.balance



def main():
    # print("Hello, this is the main method!")
    account1 = Account("Alice", 100)
    print(account1.deposit(56) ) # Outputs: 150
    # account1.withdraw(75)  # Outputs: 75

if __name__ == "__main__":
    main()
-----------------------------------------------------'''''''''
import pandas as pd
import mysql.connector

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/Harshitha/Desktop/Payroll_analytics/Payrollanalytics.ai/Python/automation/CSVs/departments.csv')

# Connect to MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='jwalaharshitha',
    password='Tredence@123',
    database='payroll_analytics_dev'
)
cursor = conn.cursor()

# Insert DataFrame into MySQL table
for _, row in df.iterrows():
    sql = "INSERT INTO departments (department_id, department_name,manager_id) VALUES (%s, %s, %s)"
    cursor.execute(sql, tuple(row))

conn.commit()
cursor.close()
conn.close()
