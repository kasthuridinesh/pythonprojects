import mysql.connector
table_create_connect = mysql.connector.connect(host='localhost', user='root', password='Atmecs@123', database="EMS")

print(table_create_connect)

create_table_cursor = table_create_connect.cursor()

create_table_cursor.execute("DROP table EMS.employee")
print("Table successfully deleted")

table_create_connect.commit()