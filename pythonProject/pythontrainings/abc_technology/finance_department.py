import ast

from abc_technology.hr_department import HumanResourceDepartment

human_resource = HumanResourceDepartment()


class FinanceDepartment:

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
                print("Employee id does not exist !!!")

        except KeyError:
            print("The given Employee detail key is invalid")
        except FileNotFoundError:
            print("The Employee detail file not exist")

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
                        print(employee_salary_details)

            # return employee_salary_details
        except KeyError:
            print("The given Employee detail key is invalid")
        except FileNotFoundError:
            print("The Employee detail file not exist")
        except UnboundLocalError:
            print("The employee id does not exist !!!")



# @staticmethod
# def add_bank_account(employee_id, bank_name, ifsc_code, account_number):
#     """
#     In this method, add the bank account of new employee by providing valid details
#         :param employee_id: should give valid employee id
#         :param bank_name: Valid bank name , should contain only alphabets and spaces
#         :param ifsc_code: Should provide valid 11 digit IFSC code
#         :param account_number: Should provide 12-digit account number
#     """
#     try:
#         bank_name = bank_name.strip()
#         bank_name_validation = bank_name.replace(" ", "")
#         ifsc_code = ifsc_code.strip()
#         account_number = account_number.strip()
#
#         if bank_name_validation.isalpha() and bank_name_validation != '' and len(ifsc_code) == 11 \
#                 and account_number.isdigit() and len(account_number) == 12:
#             bank_details = {'Bank Name': bank_name, 'IFSC code': ifsc_code,
#                             'Account Number': account_number}
#             bank_account = human_resource.get_employee_detail(employee_id, "Bank Account")
#             if bank_account == 'No':
#                 finance_department.update_employee_detail_by_id(employee_id, 'Bank Account', bank_details)
#                 print(f'Bank account detail has been successfully added')
#             else:
#                 print(f'Bank account detail has been already added!!!')
#         elif not bank_name_validation.isalpha():
#             print('The entered bank name is invalid !!!')
#         elif bank_name_validation == "":
#             print('The entered bank name is null !!!')
#         elif len(ifsc_code) != 11:
#             print('The entered ifsc code is invalid !!!')
#         else:
#             print('The entered account number is invalid !!!')
#     except FileNotFoundError:
#         print("Employee details file does not exist")
#     except AttributeError as error:
#         print(error.__doc__)
#     except TypeError as error:
#         print(error.__doc__)

finance_department = FinanceDepartment()
finance_department.get_salary_by_id()
