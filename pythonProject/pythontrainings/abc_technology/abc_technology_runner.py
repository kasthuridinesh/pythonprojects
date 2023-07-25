from abc_technology.automation_department import AutomationEngineeringDepartment
from abc_technology.finance_department import FinanceDepartment
from abc_technology.hr_department import HumanResourceDepartment
from abc_technology.it_department import ItDepartment

itdepartment = ItDepartment()
itdepartment.allocate_laptop(3)

hr = HumanResourceDepartment()
hr.add_employee()

auto = AutomationEngineeringDepartment()
auto.get_project_list()
auto.get_project_members()
auto.allocate_project_to_employee()

salary = FinanceDepartment()
salary.get_salary_by_id()
