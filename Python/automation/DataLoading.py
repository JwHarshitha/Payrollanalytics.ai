import os
import pandas as pd
from sqlalchemy import create_engine, text
import urllib.parse

# Define your connection parameters
username = 'jwalaharshitha'
password = 'Tredence@123'  # Password with special characters
host = 'localhost'
database_name = 'payroll_analytics_dev'

# URL-encode the password to handle special characters
encoded_password = urllib.parse.quote_plus(password)
connection_string = f'mysql+mysqlconnector://{username}:{encoded_password}@{host}/{database_name}'
engine = create_engine(connection_string)
folder_path = '/Users/Harshitha/Desktop/Payroll_analytics/Payrollanalytics.ai/Python/automation/Datasets'  # Adjust the folder path as needed

# Loop through all CSV files in the folder
for file_name in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file_name)
    if os.path.isfile(file_path) and file_name.endswith('.csv'):
        df = pd.read_csv(file_path)
        table_name = os.path.splitext(file_name)[0].replace('_', '')
        
        # Test the connection and process the table
        try:
            with engine.connect() as connection:
                print(f"Processing file: {file_name}")
                print(f"Connecting to table: {table_name}")
                
                # Disable foreign key checks
                connection.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
                
                # Truncate the table
                truncate_command = text(f'TRUNCATE TABLE {table_name}')
                connection.execute(truncate_command)
                print(f"Table '{table_name}' has been truncated.")
                
                # Check if the table is indeed empty
                result = connection.execute(text(f'SELECT COUNT(*) FROM {table_name}'))
                count = result.scalar()
                print(f"Number of rows in '{table_name}' after truncation: {count}")
                
                # Write the DataFrame to the MySQL table
                df.to_sql(table_name, con=engine, if_exists='append', index=False)
                print(f"Data from {file_name} has been successfully loaded into '{table_name}' table.")
                
        except Exception as e:
            print(f"An error occurred while processing {file_name}: {e}")
