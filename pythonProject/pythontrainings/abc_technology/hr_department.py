import ast


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
                                   'Gender': gender,  'Mobile Number': mobile_number,
                                   'Bank Account': 'No', 'Project': 'Resource Pool', 'Laptop Allocated': 'No',
                                   'Mobile Allocated': 'No', 'Role': role, 'Salary': salary,
                                   }
                with open('employee_details.txt', 'a') as employee_details_file:
                    employee_details_file.write(str(employee_detail))
                    employee_details_file.write('\n')
                    employee_details_file.close()
                print(f'Employee details has been added to the database and generated employee id '
                      f'for new employee is : {employee_detail.get("Employee id")}')


        except FileNotFoundError:
            print("Employee details file does not exist")

