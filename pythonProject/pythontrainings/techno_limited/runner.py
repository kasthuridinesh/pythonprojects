from hr_department import HumanResourceDepartment
from finance_department import FinanceDepartment
from it_department import ItDepartment
from automation_department import AutomationEngineeringDepartment


itdepartment = ItDepartment()
itdepartment.allocate_laptop(1)

human_resource = HumanResourceDepartment()
human_resource.show_all_employee_details()

finance_department = FinanceDepartment()
finance_department.get_salary_by_id(1)

engineering_department = AutomationEngineeringDepartment()
engineering_department.get_project_list()