from .DBConnectors import DBConnectors
import os
import pandas as pd
from sqlalchemy import text
import time

class DataLoader:
    def __init__(self):
        self.table_names = []
        self.file_names = []
        self.metrics=[]

    def data_loading_to_table(self,file_name, table_name,file_path):
        df = pd.read_csv(file_path)
        file_count=len(df)
        new_engine=DBConnectors()
        engine=new_engine.create_mysql_engine()
        with engine.connect() as connection:
            print(f"Processing file: {file_name}")
            print(f"Connecting to table: {table_name}")
            connection.execute(text("SET FOREIGN_KEY_CHECKS = 0;"))
            truncate_command = text(f'TRUNCATE TABLE {table_name}')
            connection.execute(truncate_command)
            print(f"Table '{table_name}' has been truncated.")
            insert_date = pd.Timestamp.now().date()
            start_time = time.perf_counter()
            # Write the DataFrame to the MySQL table
            df.to_sql(table_name, con=engine, if_exists='append', index=False)
            end_time = time.perf_counter()
            print(f"Data from {file_name} has been successfully loaded into '{table_name}' table.")
            load_time = (end_time - start_time) * 1000 
            result = connection.execute(text(f'SELECT COUNT(*) FROM {table_name}'))
            table_count = result.scalar()
        return (file_count,insert_date,load_time,table_count)

        
    def data_loading(self,folder_path = '/Users/Harshitha/Desktop/Payroll_analytics/Payrollanalytics.ai/Python/automation/Datasets' ):
        file_names=['attendance','benefits','bonuses','deductions','departments','employees','leave_requests','payroll','performance_reviews','positions','salaries','tax_rates','timesheets']
        table_names=['Attendance','Benefits','Bonuses','Deductions','Departments','Employees','LeaveRequests','Payroll','PerformanceReviews','Positions','Salaries','TaxRates','Timesheets']
        zipped = zip(file_names, table_names)
        zipped_list = list(zipped)
        for file_name, table_name in zipped_list:
        # Loop through all CSV files in the folder
            file_path = os.path.join(folder_path, f'{file_name}.csv')
            if os.path.isfile(file_path) and file_path.endswith('.csv'):
                source_count, created_date, load_time, table_count=self.data_loading_to_table(file_name, table_name,file_path)
                error_count=source_count-table_count
                updated_date=created_date
                self.metrics.append([table_name,file_name,source_count,table_count,error_count,load_time,created_date,updated_date])
        df_metrics = pd.DataFrame(self.metrics, columns=[
        'table_name', 'file_name', 'source_count', 'table_count', 
        'error_count', 'time_taken', 'created_date','updated_date'])
        # df_metrics['updated_date'] = None
        return df_metrics
    
    def data_quality_metrics_loading(self,summary_df):
        new_engine=DBConnectors()
        engine=new_engine.create_mysql_engine()
        with engine.connect() as connection:
            connection.execute(text('TRUNCATE TABLE DataQualityMetrics'))
            summary_df.to_sql('DataQualityMetrics', con=engine, if_exists='append', index=False)
            print("Data Quality Metrics Completed")

if __name__ == '__main__':    
    # Print or save the summary DataFrame
    DataLoading=DataLoader()
    summary_df=DataLoading.data_loading()
    DataLoading.data_quality_metrics_loading(summary_df)
    print("Loaded Data Quality Metrics")