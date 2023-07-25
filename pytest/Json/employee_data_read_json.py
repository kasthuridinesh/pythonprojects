import json
import logging

# opening Json File

f = open('employee_data.json')
data = json.load(f)
for emp_details in data["employee_details"]:
    logging.info(emp_details)

    if "employee id1" in emp_details:
        logging.info("employee id", emp_details['employee id1'])
        logging.info("employee name", emp_details['employee_name'])
        logging.info("employee lastname", emp_details['employee_lastname'])
        logging.info("Department", emp_details['Dept'])
    else:
        logging.info("There is no such details")

    if "employee_name" in emp_details:
        logging.info(emp_details['employee_name'], "and is department is", emp_details['Dept'])
    # fetching data with employee id
    if "employee_id" in emp_details:
        logging.info(emp_details['employee_id'], "and  name is", emp_details['employee_name'], "and dept is",
                     emp_details['Dept'])

# creating new file and dump all the data from another json file
new_data = json.dumps(data, indent=1)
logging.info(new_data)
