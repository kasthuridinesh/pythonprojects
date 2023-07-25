import mysql.connector
table_create_connect = mysql.connector.connect(host='localhost', user='root', password='Atmecs@123', database="EMS")

print(table_create_connect)

create_table_cursor = table_create_connect.cursor()

create_table_cursor.execute("CREATE TABLE EMS.employee(name VARCHAR(45) NULL,id INT NOT NULL,address VARCHAR(45) NULL,PRIMARY KEY (id))")
print("Table created successfully")
table_create_connect.commit()