import mysql.connector
table_create_connect = mysql.connector.connect(host='localhost', user='root', password='Atmecs@123', database="EMS")

print(table_create_connect)

create_table_cursor = table_create_connect.cursor()


create_table_cursor.execute('SELECT * FROM employee')

create_users = create_table_cursor.fetchall()

for database_user_detail in create_users:
    print(database_user_detail)
    print("name:", database_user_detail[0])
    print("id:", database_user_detail[1])
    print("address:", database_user_detail[2])


# create_table_cursor.execute('DROP database bhava')