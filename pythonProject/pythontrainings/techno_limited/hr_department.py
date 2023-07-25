import ast
from techno_limited.main import logger


class HumanResourceDepartment:

    @staticmethod
    def add_employee(name, date_of_birth, gender, address, mobile_number, role, salary, aadhar_number):

        try:
            age = date_of_birth.strip()
            name = name.strip()
            mobile_number = mobile_number.strip()
            gender = gender.strip()
            role = role.strip()
            address = address.strip()
            aadhar_number = aadhar_number.strip()
            name_validation = name.replace(" ", "").strip()
            gender_list = gender.strip()
            roles_list = role.strip()
            if mobile_number.isdigit() and name_validation.isalpha() and len(name_validation) > 2 \
                    and gender in gender_list \
                    and 9 < len(address) < 161 and role in roles_list and len(mobile_number) == 10 \
                    and salary > 0 and aadhar_number.isdigit() and len(aadhar_number) == 12:

                with open('employee_details.txt', 'r') as employee_details_file:
                    try:
                        previous_employee_detail = employee_details_file.readlines()[-1]
                        employee_details_file.close()
                        previous_employee_id = int(
                            previous_employee_detail.strip().split(',')[0].split(':')[1].strip())
                    except IndexError:
                        previous_employee_id = 0
                previous_employee_id += 1
                employee_detail = {f'Employee id': previous_employee_id, 'Name': name, 'Age': age,
                                   'Gender': gender, 'Mobile Number': mobile_number,
                                   'Bank Account': 'No', 'Project': 'Resource Pool', 'Laptop Allocated': 'No',
                                   'Mobile Allocated': 'No', 'Role': role, 'Salary': salary,
                                   }
                with open('employee_details.txt', 'a') as employee_details_file:
                    employee_details_file.write(str(employee_detail))
                    employee_details_file.write('\n')
                    employee_details_file.close()
                logger.info(f'Employee details has been added to the database and generated employee id '
                            f'for new employee is : {employee_detail.get("Employee id")}')


        except FileNotFoundError:
            logger.exception("Employee details file does not exist")

    @staticmethod
    def get_employee_all_details(employee_id):

        try:
            employee_value = None
            with open('employee_details.txt', 'r') as employee_details_file:
                employee_details_list = []
                employee_details = employee_details_file.readlines()
                for employee_detail_file in employee_details:
                    employee_details_list.append(employee_detail_file.strip())
                for employee_detail in employee_details_list:
                    employee_detail_dictionary = ast.literal_eval(employee_detail)
                    dict_employee_id = employee_detail_dictionary["Employee id"]
                    if dict_employee_id == employee_id:
                        employee_value = employee_detail_dictionary
            if employee_value is None:
                logger.info("The given employee id does not exist")

            else:
                return employee_value

        except FileNotFoundError:
            logger.exception("The Employee detail file not exist")

    @staticmethod
    def show_all_employee_details():

        try:
            with open('employee_details.txt', 'r') as employee_details_file:
                employee_details = employee_details_file.readlines()
                for employee_detail in employee_details:
                    print(employee_detail)
        except FileNotFoundError:
            logger.exception("The Employee details not found")

    def get_employee_detail(employee_id, employee_key):

        try:
            employee_value = None
            with open('employee_details.txt', 'r') as employee_details_file:
                employee_details_list = []
                employee_details = employee_details_file.readlines()
                for employee_detail_file in employee_details:
                    employee_details_list.append(employee_detail_file.strip())
                for employee_detail in employee_details_list:
                    employee_detail_dictionary = ast.literal_eval(employee_detail)
                    dict_employee_id = employee_detail_dictionary["Employee id"]
                    if dict_employee_id == employee_id:
                        employee_value = employee_detail_dictionary[employee_key]
                if employee_value is None:
                    logger.info("The given employee id does not exist")

                else:
                    return employee_value

        except FileNotFoundError:
            logger.info("The Employee detail file not exist")

    @staticmethod
    def get_employee_detail(employee_id, employee_key):

        try:
            employee_value = None
            with open('employee_details.txt', 'r') as employee_details_file:
                employee_details_list = []
                employee_details = employee_details_file.readlines()
                for employee_detail_file in employee_details:
                    employee_details_list.append(employee_detail_file.strip())
                for employee_detail in employee_details_list:
                    employee_detail_dictionary = ast.literal_eval(employee_detail)
                    dict_employee_id = employee_detail_dictionary["Employee id"]
                    if dict_employee_id == employee_id:
                        employee_value = employee_detail_dictionary[employee_key]
                if employee_value is None:
                    logger.info("The given employee id does not exist")

                else:
                    return employee_value

        except FileNotFoundError:
            logger.exception("The Employee detail file not exist")

# human_resource = HumanResourceDepartment()
# human_resource.show_all_employee_details()
