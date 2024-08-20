
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
-----------------------------------------------------
import pandas as pd
import mysql.connector

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/Harshitha/Desktop/Payroll_analytics/Payrollanalytics.ai/Python/automation/Datasets/departments.csv')

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
--------------------------------------------------------------
import pandas as pd

from sqlalchemy import create_engine,text
import urllib.parse

# Load the CSV file into a DataFrame
df = pd.read_csv('/Users/Harshitha/Desktop/Payroll_analytics/Payrollanalytics.ai/Python/automation/Datasets/departments.csv')
# Define your connection parameters
username = 'jwalaharshitha'
password = 'Tredence@123'  # Password with special characters
host = 'localhost'
database_name = 'payroll_analytics_dev'

# URL-encode the password to handle special characters
encoded_password = urllib.parse.quote_plus(password)

# Create the connection string
connection_string = f'mysql+mysqlconnector://{username}:{encoded_password}@{host}/{database_name}'

# Create the engine
engine = create_engine(connection_string)
table_name= 'departments'
# Test the connection
try:
    with engine.connect() as connection:
        print("Connection to the database was successful!")
        connection.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
        truncate_command = text(f'TRUNCATE TABLE {table_name}')
        connection.execute(truncate_command)
        # connection.execute(f'TRUNCATE {table_name}')
        print(f"Table '{table_name}' has been truncated.")

        # Check if the table is indeed empty
        result = connection.execute(text(f'SELECT COUNT(*) FROM {table_name}'))
        count = result.scalar()
        print(f"Number of rows in '{table_name}' after truncation: {count}")

        # Write the DataFrame to the MySQL table
        df.to_sql(table_name, con=engine, if_exists='append', index=False)
       
except Exception as e:
    print(f"An error occurred: {e}")
-------------------------------------------------------'''''''''

