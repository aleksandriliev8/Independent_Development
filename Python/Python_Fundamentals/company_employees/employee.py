class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee(Employee):
    def __init__(self, fname, lname, _salary):
        super().__init__(fname, lname)
        self.salary = _salary
    
    def calculate_paycheck(self):
        return self.salary / 52
    
class HourlyEmployee(Employee):
    def __init__(self, fname, lname, weekly_hours, hourly_rate):
        super().__init__(fname, lname)
        self.weekly_hours = weekly_hours
        self.hourly_rate = hourly_rate

    def calculate_paycheck(self):
        return self.weekly_hours * self.hourly_rate
    
class CommisionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, _salary, sales_num, com_rate):
        super().__init__(fname, lname, _salary)
        self.sales_num = sales_num
        self.com_rate = com_rate

    def calculate_paycheck(self):
        regular_salary = super().calculate_paycheck()
        total_commision = self.sales_num * self.com_rate
        return regular_salary + total_commision