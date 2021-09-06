import logging
from hr import PayrollSystem
from productivity import ProductivitySystem
from contacts import AddressBook
from abc import ABC, abstractmethod


class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {
                'id': 1,
                'name': '1',
                'role': 'manager'
            },
            {
                'id': 2,
                'name': '2',
                'role': 'secretary'
            },
            {
                'id': 3,
                'name': '3',
                'role': 'sales'
            },
            {
                'id': 4,
                'name': '4',
                'role': 'factory'
            },
            {
                'id': 5,
                'name': '5',
                'role': 'secretary'
            },
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook()

    def employees(self):
        return [self._create_employee(**data) for data in self._employees]


    def _create_employee(self, id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)
"""
abstract class

class Employee(ABC):
    def __init__(self, id, name):
        self.id = id
        self.name = name
        logging.info(f"initialized employee {self.id}  {self.name}")

    @abstractmethod
    def calculate_payroll(self):
        pass
"""
class Employee:
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self.role = role
        self.payroll = payroll
        logging.info(f"initialized employee {self.id}  {self.name}")

    def work(self, hours):
        duties = self.role.work(hours)
        logging.info(f"{self.id} - {self.name}")
        logging.info(f"{duties}")
        self.payroll.track_work(hours)

    def calculate_payroll(self):
        return self.payroll.calculate_payroll()
#
#
# class SalaryEmployee(Employee):
#     def __init__(self, id, name, weekly_salary):
#         super().__init__(id, name)
#         self.weekly_salary = weekly_salary
#         logging.info(f"initialized salary employee {self.id}  {self.name}")
#
#     def calculate_payroll(self):
#         return self.weekly_salary
#
# class HourlyEmployee(Employee):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         super().__init__(id, name)
#         self.hours_worked = hours_worked
#         self.hour_rate = hour_rate
#         logging.info(f"initialized hourly employee {self.id}  {self.name}")
#
#     def calculate_payroll(self):
#         return self.hours_worked * self.hour_rate
#
# class CommissionEmployee(SalaryEmployee):
#     def __init__(self, id, name, weekly_salary, commission):
#         super().__init__(id,  name, weekly_salary)
#         self.commission = commission
#         logging.info(f"initialized commission employee {self.id}  {self.name}")
#
#     def calculate_payroll(self):
#         fixed = super().calculate_payroll()
#         return fixed + self.commission
#
# """class Manager(SalaryEmployee):
#     def work(self, hours):
#         logging.info(f"{self.name} manages for {hours} hours")
# """
# class Manager(Employee, ManagerRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         super().__init__(id, name)
#
#
# """class Secretary(SalaryEmployee):
#     def work(self, hours):
#         logging.info(f"{self.name} does paperwork for {hours} hours")
# """
# class Secretary(Employee, SecretaryRole, SalaryPolicy):
#     def __init__(self, id, name, weekly_salary):
#         SalaryPolicy.__init__(self, weekly_salary)
#         super().__init__(id, name)
#
#
# """
# each class has its own MRO (method resolution order) - c3 linearization
# resolution of class without init
#
# class TemporarySecretary(Secretary, HourlyEmployee):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyEmployee.__init__(self, id, name, hours_worked, hour_rate)
#
#     def calculate_payroll(self):
#         return HourlyEmployee.calculate_payroll(self)
# """
# class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyPolicy.__init__(self, hours_worked, hour_rate)
#         super().__init__(id, name)
#
# """
# class SalesPerson(CommissionEmployee):
#     def work(self, hours):
#         logging.info(f"{self.name} on the phone for {hours} hours")
# """
# class SalesPerson(Employee, SalesRole, CommissionPolicy):
#     def __init__(self, id, name, weekly_salary, commission):
#         CommissionPolicy.__init__(self, weekly_salary, commission)
#         super().__init__(id, name)
#
# """
# class FactoryWorker(HourlyEmployee):
#     def work(self, hours):
#         logging.info(f"{self.name} manufactures for {hours} hours")
# """
# class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
#     def __init__(self, id, name, hours_worked, hour_rate):
#         HourlyPolicy.__init__(self, hours_worked, hour_rate)
#         super().__init__(id, name)
