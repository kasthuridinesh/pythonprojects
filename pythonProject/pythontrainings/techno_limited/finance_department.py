import ast

from techno_limited.hr_department import HumanResourceDepartment
from techno_limited.main import logger

human_resource = HumanResourceDepartment()


class FinanceDepartment:
    @staticmethod
    def update_employee_detail_by_id(employee_id, update_detail_key, update_detail_value):

        employee_id_exist = False
        try:
            with open('employee_details.txt', 'r') as employee_details_file:
                employee_details_list = []
                employee_details = employee_details_file.readlines()
                employee_details_file.close()
                for employee_detail_file in employee_details:
                    employee_details_list.append(employee_detail_file.strip())
                for index, employee_detail in enumerate(employee_details_list):
                    employee_detail_dictionary = ast.literal_eval(employee_detail)
                    dict_employee_id = employee_detail_dictionary["Employee id"]
                    if dict_employee_id == employee_id:
                        employee_detail_dictionary[update_detail_key] = update_detail_value
                        employee_details_list[index] = employee_detail_dictionary
                        employee_id_exist = True
            if employee_id_exist:
                with open('employee_details.txt', 'w') as employee_details_file:
                    employee_details_file.write("")
                    employee_details_file.close()
                with open('employee_details.txt', 'a') as employee_details_file:
                    for employee_detail in employee_details_list:
                        employee_details_file.write(str(employee_detail))
                        employee_details_file.write('\n')
                    employee_details_file.close()
            else:
                logger.info("Employee id does not exist !!!")

        except KeyError:
            logger.exception("The given Employee detail key is invalid")
        except FileNotFoundError:
            logger.exception("The Employee detail file not exist")

    @staticmethod
    def get_salary_by_id(employee_id):

        try:
            with open('employee_details.txt', 'r') as employee_details_file:
                employee_details_list = []
                employee_details = employee_details_file.readlines()
                employee_details_file.close()
                for employee_detail_file in employee_details:
                    employee_details_list.append(employee_detail_file.strip())
                for index, employee_detail in enumerate(employee_details_list):
                    employee_detail_dictionary = ast.literal_eval(employee_detail)
                    dict_employee_project = employee_detail_dictionary["Employee id"]
                    if dict_employee_project == employee_id:
                        employee_salary_details = "The salary for " + employee_detail_dictionary.get("Name") + \
                                                  " is " + str(employee_detail_dictionary.get("Salary")) + \
                                                  " and his role is " + employee_detail_dictionary.get("Role")
                        logger.info(employee_salary_details)

            # return employee_salary_details
        except KeyError:
            logger.info("The given Employee detail key is invalid")
        except FileNotFoundError:
            logger.info("The Employee detail file not exist")
        except UnboundLocalError:
            logger.info("The employee id does not exist !!!")

# finance_department = FinanceDepartment()
# finance_department.get_salary_by_id(1)
