import ast
from operator import itemgetter

from abc_technology.finance_department import FinanceDepartment

finance_department = FinanceDepartment()


class AutomationEngineeringDepartment:

    def get_project_members(self,project):

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
                            print(project_members, employee_count)
                return project_members, employee_count


            except KeyError:
                print("The given Employee detail key is invalid")
        else:
            print('The entered project is invalid')
            exit()

    def get_project_list(project):
        project_list = ['Zscalar', 'waterloop', 'Nano', 'Raw']
        print(project_list)
        return project_list

    def get_roles_list(project):

        roles_list = ['Engineer', 'Team Lead', 'Manager', 'Vice President']
        print(roles_list)
        return roles_list

    def allocate_project_to_employee(employee_id, project):

        if project in engineering_department.get_project_list():
            finance_department.update_employee_detail_by_id(employee_id, 'Project', project)
            print(f'Employee id : {employee_id} has been allocated to project {project}')
        else:
            project_list = engineering_department.get_project_list()
            print(f'The project {project} is invalid !!! The available projects are '
                  f'{project_list}')


engineering_department = AutomationEngineeringDepartment()
engineering_department.get_project_list()
