import logging
import employees

""" do no instantiate this class """
class _ProductivitySystem:
    def __init__(self):
        """ underscore dont access outside the class """
        self._roles = {
            'manager': ManagerRole,
            'secretary': SecretaryRole,
            'sales': SalesRole,
            'factory': FactoryRole
        }

    def track(self, employees, hours):
        logging.info('Tracking productivity')
        for employee in employees:
            result = employee.work(hours)

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError("invalid role_id")
        return role_type()

class ManagerRole:
    def work(self, hours):
        logging.info("manager working")
        return "manager working"

class SecretaryRole:
    def work(self, hours):
        logging.info("secretary working")
        return "secretary working"

class SalesRole:
    def work(self, hours):
        logging.info("sales working")
        return "sales working"

class FactoryRole:
    def work(self, hours):
        logging.info("factory working")
        return "factory working"

_productivity_system = _ProductivitySystem()

""" public interfaceto productivity system """
def get_role(role_id):
    return _productivity_system.get_role(role_id)

def track(employees, hours):
    return _productivity_system.track(employees, hours)
