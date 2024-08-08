CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`Departments` (
  `department_id` INT NOT NULL AUTO_INCREMENT,
  `department_name` VARCHAR(45) NULL,
  `manager_id` INT NULL,
  PRIMARY KEY (`department_id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`Employees` (
  `employee_id` INT NOT NULL,
  `first_name` VARCHAR(45) NULL,
  `last_name` VARCHAR(45) NULL,
  `date_of_birth` DATE NULL,
  `gender` ENUM('female', 'male', 'other') NULL,
  `hire_date` DATE NULL,
  `department_id` INT NULL,
  `position` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `phone` INT(30) NULL,
  `address` VARCHAR(250) NULL,
  PRIMARY KEY (`employee_id`),
  INDEX `department_id_idx` (`department_id` ASC) VISIBLE,
  CONSTRAINT `department_id`
    FOREIGN KEY (`department_id`)
    REFERENCES `payroll_analytics_dev`.`Departments` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`Positions` (
  `Position_id` INT NOT NULL AUTO_INCREMENT,
  `Position_name` VARCHAR(45) NULL,
  `department_id` INT NULL,
  `base_salary` DECIMAL(10,2) NULL,
  PRIMARY KEY (`Position_id`),
  INDEX `department_id_idx` (`department_id` ASC) VISIBLE,
  CONSTRAINT `department_id_check`
    FOREIGN KEY (`department_id`)
    REFERENCES `payroll_analytics_dev`.`Departments` (`department_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`SDepartmentsalaries` (
  `salary_id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NULL,
  `base_salary` DECIMAL(10,2) NULL,
  `bonus` DECIMAL(10,2) NULL,
  `deductions` DECIMAL(10,2) NULL,
  `pay_date` DATE NULL,
  PRIMARY KEY (`salary_id`),
  INDEX `employee_id_salariesCnstrnt_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `employee_id_salariesCnstrnt`
    FOREIGN KEY (`employee_id`)
    REFERENCES `payroll_analytics_dev`.`employees` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`Bonuses` (
  `bonus_id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NULL,
  `bonus_amount` DECIMAL(10,2) NULL,
  `reason` VARCHAR(255) NULL,
  `date_given` DATE NULL,
  PRIMARY KEY (`bonus_id`),
  INDEX `empID_bonus_Cnstrnt_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `empID_bonus_Cnstrnt`
    FOREIGN KEY (`employee_id`)
    REFERENCES `payroll_analytics_dev`.`employees` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`Deductions` (
  `deduction_id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NULL,
  `deduction_type` VARCHAR(45) NULL,
  `deduction_amount` DECIMAL(10,2) NULL,
  `effective_date` DATE NULL,
  PRIMARY KEY (`deduction_id`),
  INDEX `empID_deduction_Cnstrnt_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `empID_deduction_Cnstrnt`
    FOREIGN KEY (`employee_id`)
    REFERENCES `payroll_analytics_dev`.`employees` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`Payroll` (
  `payroll_id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NULL,
  `pay_period_start` DATE NULL,
  `pay_period_end` DATE NULL,
  `total_hours_worked` DECIMAL(5,2) NULL,
  `overtime_hours` DECIMAL(5,2) NULL,
  `gross_pay` DECIMAL(10,2) NULL,
  `net_pay` DECIMAL(10,2) NULL,
  `pay_date` DATE NULL,
  PRIMARY KEY (`payroll_id`),
  INDEX `empid_payroll_cnstrnt_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `empid_payroll_cnstrnt`
    FOREIGN KEY (`employee_id`)
    REFERENCES `payroll_analytics_dev`.`employees` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`Timesheets` (
  `timesheet_id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NULL,
  `date` DATE NULL,
  `hours_worked` DECIMAL(5,2) NULL,
  `overtime_hours` DECIMAL(5,2) NULL,
  PRIMARY KEY (`timesheet_id`),
  INDEX `empid_timesheets_cnstnt_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `empid_timesheets_cnstnt`
    FOREIGN KEY (`employee_id`)
    REFERENCES `payroll_analytics_dev`.`employees` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`Attendance` (
  `attendance_id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NULL,
  `date` DATE NULL,
  `status` ENUM('present', 'absent', 'leave') NULL,
  PRIMARY KEY (`attendance_id`),
  INDEX `empid_attendance_cnstrnt_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `empid_attendance_cnstrnt`
    FOREIGN KEY (`employee_id`)
    REFERENCES `payroll_analytics_dev`.`employees` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`LeaveRequests` (
  `leave_request_id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NULL,
  `leave_type` VARCHAR(50) NULL,
  `start_date` DATE NULL,
  `end_date` DATE NULL,
  `reason` TEXT(500) NULL,
  `status` ENUM('Approved', 'Pending', 'Rejected') NULL,
  PRIMARY KEY (`leave_request_id`),
  INDEX `empid_LeaveRequest_Cnstrnt_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `empid_LeaveRequest_Cnstrnt`
    FOREIGN KEY (`employee_id`)
    REFERENCES `payroll_analytics_dev`.`employees` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`Benefits` (
  `benefit_id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NULL,
  `benefit_type` VARCHAR(50) NULL,
  `benefit_amount` DECIMAL(10,2) NULL,
  `start_date` DATE NULL,
  `end_date` DATE NULL,
  PRIMARY KEY (`benefit_id`),
  INDEX `empid_benefits_cnstrnt_idx` (`employee_id` ASC) VISIBLE,
  CONSTRAINT `empid_benefits_cnstrnt`
    FOREIGN KEY (`employee_id`)
    REFERENCES `payroll_analytics_dev`.`employees` (`employee_id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`TaxRates` (
  `taxrate_id` INT NOT NULL AUTO_INCREMENT,
  `effective_date` DATE NULL,
  `tax_rate` DECIMAL(5,2) NULL,
  PRIMARY KEY (`taxrate_id`))
ENGINE = InnoDB;

CREATE TABLE IF NOT EXISTS `payroll_analytics_dev`.`PerformanceReviews` (
  `review_id` INT NOT NULL AUTO_INCREMENT,
  `employee_id` INT NULL,
  `review_date` DATE NULL,
  `performance_score` DECIMAL(3,2) NULL,
  `comments` TEXT(100) NULL,
  PRIMARY KEY (`review_id`))
ENGINE = InnoDB;