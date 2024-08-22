import os
import pandas as pd
from sqlalchemy import create_engine, text
import urllib.parse
import time

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

class DataLoader:
    def __init__(self):
        self.table_names = []
        self.file_names = []
        self.row_counts = []
        self.file_count = 0
        self.table_count = 0
        # self.error_count = 0
        self.insert_dates = []
        self.load_times = []

        
    def data_loading(self):
    # Loop through all CSV files in the folder
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if os.path.isfile(file_path) and file_name.endswith('.csv'):
                df = pd.read_csv(file_path)
                self.file_count+=1
                table_name = os.path.splitext(file_name)[0].replace('_', '')
                self.table_count+=1
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
                        
                        insert_date = pd.Timestamp.now().date()
                        start_time = time.perf_counter()
                        # Write the DataFrame to the MySQL table
                        df.to_sql(table_name, con=engine, if_exists='append', index=False)
                        end_time = time.perf_counter()
                        print(f"Data from {file_name} has been successfully loaded into '{table_name}' table.")
                        
                        load_time = (end_time - start_time) * 1000 
                        error_count=self.file_count-self.table_count
                        # Append the table name, row count, and insert date to the lists
                        
                        self.file_names.append(file_name)
                        self.table_names.append(table_name)
                        self.row_counts.append(count)
                        self.insert_dates.append(insert_date)
                        self.load_times.append(load_time)

                except Exception as e:
                    print(f"An error occurred while processing {file_name}: {e}")

        self.summary_df = pd.DataFrame({
            'table_name': self.table_names,
            'file_name': self.file_names,
            # 'Row Count': self.row_counts,
            'source_count':self.file_count,
            'table_count':self.table_count,
            'error_count':error_count,
            'time_taken':self.load_times,
            'created_date': self.insert_dates,
            'updated_date':None
        })
        return self.summary_df

def data_quality_metrics(summary_df):
    summary_df.to_sql('DataQualityMetrics', con=engine, if_exists='append', index=False)


if __name__ == '__main__':    
    # Print or save the summary DataFrame
    DataLoading=DataLoader()
    summary_df=DataLoading.data_loading()
    data_quality_metrics(summary_df)
    # summary_df.shape
    print("Loaded Data Quality Metrics")