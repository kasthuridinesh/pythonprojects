import mysql.connector
table_create_connect = mysql.connector.connect(host='localhost', user='root', password='Atmecs@123', database="EMS")

print(table_create_connect)

create_table_cursor = table_create_connect.cursor()

update_table = "UPDATE EMS.employee SET name = 'John', address = 'USA' WHERE id = 2"
create_table_cursor.execute(update_table)
table_create_connect.commit()
print("Table updated successfully")
