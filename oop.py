import concurrent.futures
import logging
import hr
import employees
import productivity
import contacts

def init():
    try:
        logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(process)d - %(levelname)s - %(message)s")
        logging.info("app initialized")
    except:
        logging.exception("failed to initialize app")
        return False
    return True

def  main():
    logging.info("main started")
    payroll_system = hr.PayrollSystem()
    salary_employee = employees.SalaryEmployee(1, "John Smith", 1500)
    hourly_employee = employees.HourlyEmployee(2, 'Jane Doe', 40, 15)
    commission_employee = employees.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)

    try:
        workers = [salary_employee, hourly_employee, commission_employee]

        manager = employees.Manager(1, 'manager', 1500)
        manager.address = contacts.Address('121 manager address', 'city', 'state', '00001')
        secretary = employees.Secretary(2, 'secretary', 1200)
        secretary.address = contacts.Address('121 secretary address', 'city', 'state', '00001')
        sales_guy = employees.SalesPerson(3, 'sales', 1000, 250)
        factory_worker = employees.FactoryWorker(4, 'worker', 40, 15)
        temporary_secretary = employees.TemporarySecretary(5, 'temporary secretary', 40, 9)
        logging.info(employees.TemporarySecretary.__mro__)

        workers = [manager, secretary, sales_guy, factory_worker, temporary_secretary]

        productivity_system = productivity.ProductivitySystem()
        productivity_system.track(workers, 40)
        payroll_system.calculate_payroll(workers)
    except:
        logging.exception("Fatal error")

    logging.info("main ended")
if __name__ == "__main__":
    if init():
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as worker:
            worker.submit(main)
    logging.info("app finished")
