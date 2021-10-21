from random import randint

class EmployeeProcessor:

    def generate_employee_id(self, first_name, last_name):
        return f'{first_name[:4].lower()}{last_name[:4].lower()}{randint(100, 999)}'