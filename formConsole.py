from drydemolibrary import EmployeeProcessor

first_name = input('First name [Martha]:') or 'Martha'
last_name = input('Last name [Jones]:') or 'Jones'

processor = EmployeeProcessor()
print(processor.generate_employee_id(first_name, last_name))
