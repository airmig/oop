import logging
import employees
import productivity
import hr
import json

def print_dict(d):
    return(json.dumps(d, indent=2))


try:
    logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(process)d - %(levelname)s - %(message)s")
    workers = employees.employee_database.employees()
    productivity.track(workers, 40)
    hr.calculate_payroll(workers)

    temp_secretary = employees.Employee(5)
    logging.info(dir(temp_secretary))
    logging.info(print_dict(temp_secretary.to_dict()))

except:
    logging.exception("Fatal error")
