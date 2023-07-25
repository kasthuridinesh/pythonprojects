import ast
from operator import itemgetter
from techno_limited.main import logger

from techno_limited.finance_department import FinanceDepartment

finance_department = FinanceDepartment()


class AutomationEngineeringDepartment:

    def get_project_members(project):

        employee_count = 0
        project_members = []
        if project in engineering_department.get_project_list():
            try:
                with open('employee_details.txt', 'r') as employee_details_file:
                    employee_details_list = []
                    employee_details = employee_details_file.readlines()
                    employee_details_file.close()
                    for employee_detail_file in employee_details:
                        employee_details_list.append(employee_detail_file.strip())
                    for index, employee_detail in enumerate(employee_details_list):
                        employee_detail_dictionary = ast.literal_eval(employee_detail)
                        dict_employee_project = employee_detail_dictionary["Project"]
                        if dict_employee_project == project:
                            employee_count += 1
                            project_members.append(itemgetter('Employee id', 'Name')(employee_detail_dictionary))
                return project_members, employee_count

            except KeyError:
                logger.exception("The given Employee detail key is invalid")
        else:
            logger.exception('The entered project is invalid')

    def get_project_list(project):

        project_list = ['Zscalar', 'Hyperloop', 'Nice', 'Resource Pool']
        logger.info(project_list)
        return project_list

    def get_roles_list(project):

        roles_list = ['Engineer', 'Team Lead', 'Manager', 'Vice President']
        return roles_list

    @staticmethod
    def allocate_project_to_employee(employee_id, project):

        if project in engineering_department.get_project_list():
            finance_department.update_employee_detail_by_id(employee_id, 'Project', project)
            print(f'Employee id : {employee_id} has been allocated to project {project}')
        else:
            project_list = engineering_department.get_project_list()
            logger.info(f'The project {project} is invalid !!! The available projects are '
                        f'{project_list}')


engineering_department = AutomationEngineeringDepartment()
engineering_department.get_project_list()
