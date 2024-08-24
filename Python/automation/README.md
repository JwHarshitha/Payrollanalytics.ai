###### Payrollanalytics.ai
##About the Project
Payrollanalytics.ai had the different csv files containing the data of employees of an organization, their salaries and their financial/official details. These CSV files are loaded into the MySQL tables and the mretrics of these tables are then loaded into a final table called Data Quality Metrics.

##Built With
.Python Language
.MySQL Database

##Getting Started
In order to run the project, you need to the following.

#Pre-requisites
Install all the packages present in requirements.txt

#Usage
.DataGenerator:
 This file is used to generate the data of the employees in CSV files

 .DBConnectors:
 This file is used to create an engine of SQLAlchemy to connect with MySQl Database.

.DataLoader:
This file creates the engine using DBConnectors file and loads the data in CSV's to the MySQL tables that were created previously.
The basic details/metadata of these tables is then loaded into the final table called as Data Quality Metrics.  