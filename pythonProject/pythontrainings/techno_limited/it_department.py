
from techno_limited.finance_department import FinanceDepartment
from techno_limited.hr_department import HumanResourceDepartment
from techno_limited.main import logger

finance_department = FinanceDepartment()
human_resource = HumanResourceDepartment()


class ItDepartment:
    @staticmethod
    def allocate_laptop(employee_id):

        laptop_status = human_resource.get_employee_detail(employee_id, "Laptop Allocated")
        if laptop_status == 'No':
            finance_department.update_employee_detail_by_id(employee_id, 'Laptop Allocated', 'Yes')
            logger.info(f"Laptop has been assigned to the employee id : {employee_id}")
        else:
            logger.info(f'Laptop has been already allocated to the employee id : {employee_id}')




# itdepartment = ItDepartment()
# itdepartment.allocate_laptop(1)
