from Python.automation.DataGenerator import DataGenerator
from Python.automation.DataLoader import DataLoader

def main():
    # Generate Employees
    data_generator = DataGenerator()
    data_generator.generate_employees()
    # Generate Departments
    data_generator.generate_departments()
    # Generate Positions
    data_generator.generate_positions()
    # Generate Salaries
    data_generator.generate_salaries()
    # Generate Payrolls
    data_generator.generate_payrolls()
    # Generate Timesheets
    data_generator.generate_timesheets()
    # Generate Attendance
    data_generator.generate_attendances()
    # Generate leave_requests
    data_generator.generate_leave_requests()
    # Generate benefits
    data_generator.generate_benefits()
    # Generate TaxRates
    data_generator.generate_tax_rates()
    # Generate deductions
    data_generator.generate_deductions()
    # Generate performance_reviews
    data_generator.generate_performance_reviews()
    # Generate bonuses
    data_generator.generate_bonuses()
    print("CSV's generated successfully")

    DataLoading=DataLoader()
    DataLoading.data_loading()
    print("Loaded Data Quality Metrics")

if __name__ == "__main__":
    main()