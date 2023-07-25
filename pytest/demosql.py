#*************************CREATE NEW DATABASE and SHOW DATABASE******************
import mysql.connector

myconnect = mysql.connector.connect(host='localhost', user='root', password='Atmecs@123')

print(myconnect)

mycursor = myconnect.cursor()

mycursor.execute("CREATE SCHEMA `employee`")

# mycursor.execute("SHOW SCHEMAS")
# for db in mycursor:
#     print(db)

